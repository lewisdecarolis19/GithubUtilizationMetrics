#Libraries to import
import json                       #Parses Json into python dictionary                    
import requests                   #Executes api requests   
from pandas import json_normalize #Allows json to be normallized into flat table
import pandas as pd               #Data analysis tools, structures (dataframes)


#Make a request for a session for the REST API using our token

#Store parameters for our requested session
gh_session      = requests.Session()  

#Authorization token for the request.  Change token here as needed
gh_session.auth = ('username', 'bearer_token')   

github_api      = 'https://api.github.com'
owner           = 'owner'
page_number     = 1

#Repos are in a list so that we can loop through.  This will be the inner part of our nested loops
repos           = ['repo1','repo2']

#Github_api variable contains {} signifying dynamic parameters will be placed here in the upcoming functions
#Endpoints are in a list so we can loop through all of them
#See Github endpoints documentation for more information: https://docs.github.com/en/rest?apiVersion=2022-11-28

endpoints       = ['/repos/{}/{}/contributors?page={}&per_page=100',
                   '/repos/{}/{}/commits?page={}&per_page=100',
                   '/repos/{}/{}/pulls?page={}&per_page=100&state=all',
                   '/repos/{}/{}/pulls/comments?page={}&per_page=100']



#Loops through each endpoint (4) and repo (2 per endpoint) to retrieve our results from GH.  Append and concatenate specified DFs to obtain a list of DFs (1 per endpoint)

dataframe  = []                       #Append the two repo DFs for each endpoint into this list (happens at the end of the loop)

dataframes = []                       #Append the concatenated DF (both repos in 1 DF) for each enpoint (happends at the end of the loop)                                                                                    

#Nested for loops to iterate through each endpoint, and each repo for each endpoint.  There will be a total of eight passes (4 endpoints * 2 repos each)
for x in range(len(endpoints)):       #Begins the for loop for each of our endpoints listed in our variable in the cell above
    endpoint = endpoints[x]           #This will be the value of the endpoint, dynamic and dependant on loop iteration
    
    for y in range(len(repos)):       #Begins the nested for loop for each repo of each endpoint
        repo = repos[y]               #This will be the value of the repo, dynamic and dependant on loop iteration in the endpoint
    
        #Wraps the data extraction into a function so multiple pages can be pulled using a page parameter, paignation.  Note that the tabs/spacing is important since we are in a loops
        def github_api_get_data(repo, owner, github_api):                                          #Function name and parameters (repo is based on the iteration in our loop)
            array = []                                                                             #Array that will be returned
            next = True                                                                            #Next item in iterator
            i = 1                                                                                  #This will add 1 each time for a new page 
            while next == True:                                                                    #While loop, == is used to check equality
                url = github_api + endpoint.format(owner, repo, i)                                 #Endpoint, uses parameters (repo is based on the iteration in our loop)
                pg = gh_session.get(url = url)        
                pg_list = [dict(item, **{'repo_name':'{}'.format(repo)}) for item in pg.json()]    #Returns object for repo
                pg_list = [dict(item, **{'owner':'{}'.format(owner)}) for item in pg_list]         #Returns object for owner
                array = array + pg_list 
                if 'Link' in pg.headers:
                    if 'rel="next"' not in pg.headers['Link']:                                     #Checks this link parameter for "next"value
                        next = False                                                               #If no \"next\", then stop while loop
                i = i + 1                                                                          #Page variable counts up 1
            return array                                                                           #Returns values in a list
       
        #Creates another function to normalize the JSON and create the dataframe from the function above. Note that the tabs/spacing is important since we are in a loops
        def github_create_df(repo, owner, github_api):                                             #Function name and parameters (repo is based on the iteration in our loop)
            list = github_api_get_data(repo, owner, github_api)                                    #Uses function from previous cell
            return json_normalize(list)

        df = github_create_df(repo, owner, github_api)                                     #Creates the flat table using the function
        dataframe.append(df)                                                              #Appends the dataframe above to our list "dataframe". Only 2 DFs will be in here at 1 time.  DF per repo per endpoint  
        
        #End of the Repo Loop per each endpoint.  Spacing is important here

    #We are now only in the first loop per each endpoint
    
    #Concatenates the two repo DFs for our endpoint together into 1 DF.  Still in the first loop (per endpoint), which is important (ie spacing is important)
    df2 = pd.concat(dataframe, ignore_index=True)               #Concatenates the two dataframes in our list together to get 1 dataframe
    dataframes.append(df2)                                      #Appends the concatenated DF to our "dataframes" list.  There will be 4 DFs here, 1 per endpoint
        

    dataframe = []                                       #WE ARE STILL IN THE LOOP PER ENDPOINT. Overwrite the 2 DFs in "dataframe" so that the next endpoint can put its repo DFs there and concatenate properly
    #End of the Endpoint for loop.  Anything outside of the loop should not be tabbed or spaced in


#Manipulate the contributors dataframe

#Pull the contributors from our list of dataframes - First dataframe in the list
df_contributor  = dataframes[0]

#We will have duplicate contributors in our df, each person would have a row per repo.  We want to merge by the user name. 1 row per contributor
#Group our records by the user_id.  We groupby three columns because each will be unique by user, and we want to keep all of them.  The rest of the columns will be dropped
#We then aggregate the contributions column by user, adding the contributions in both repos per user together
df_contributors = df_contributor.groupby(['id', 'login', 'node_id'])['contributions'].agg('sum')


#Manipulate the commits dataframe

#Pull the commits from our list of dataframes - Second dataframe in the list
df_commit = dataframes[1]

#Date Columns
df_commit['date']               =  pd.to_datetime(df_commit['commit.committer.date'])
df_commit['date']               =  pd.to_datetime(df_commit['date'], utc=True)
df_commit['commit_date']        = df_commit['date'].dt.date
df_commit['commit_year']        = df_commit['date'].dt.year
df_commit['commit_month']       = df_commit['date'].dt.month
df_commit['commit_day']         = df_commit['date'].dt.day
df_commit['commit_day_of_week'] = df_commit['date'].dt.dayofweek

#Drop the datetime column, cannot write an excel file with timezone in datetime column
df_commits = df_commit.drop('date', axis=1)


#Manipulate the pull requests dataframe

#Pull the PRs from our list of dataframes - Third dataframe in the list
df_pull = dataframes[2]

#Date Columns
df_pull['date']           = pd.to_datetime(df_pull['created_at'])
df_pull['date']           = pd.to_datetime(df_pull['date'], utc=True)
df_pull['pr_date']        = df_pull['date'].dt.date
df_pull['pr_year']        = df_pull['date'].dt.year
df_pull['pr_month']       = df_pull['date'].dt.month
df_pull['pr_day']         = df_pull['date'].dt.day
df_pull['pr_day_of_week'] = df_pull['date'].dt.dayofweek

#Drop the datetime column, cannot write an excel file with timezone in datetime column
df_pulls = df_pull.drop('date', axis=1)


#Manipulate the pull request comments dataframe

#Pull the PR comments from our list of dataframes - Fourth dataframe in the list
df_pull_comments = dataframes[3]

#Date Columns
df_pull_comments['date']                = pd.to_datetime(df_pull_comments['created_at'])
df_pull_comments['date']                = pd.to_datetime(df_pull_comments['date'], utc=True)
df_pull_comments['comment_date']        = df_pull_comments['date'].dt.date
df_pull_comments['comment_year']        = df_pull_comments['date'].dt.year
df_pull_comments['comment_month']       = df_pull_comments['date'].dt.month
df_pull_comments['comment_day']         = df_pull_comments['date'].dt.day
df_pull_comments['comment_day_of_week'] = df_pull_comments['date'].dt.dayofweek

#Drop the datetime column, cannot write an excel file with timezone in datetime column
df_pull_comments = df_pull_comments.drop('date', axis=1)


#Writes to a single excel file.  Each df becomes its own sheet in the excel file
with pd.ExcelWriter('filepath/github_data.xlsx') as writer:  
     df_contributors.to_excel(writer, sheet_name='Contributors') 
     df_commits.to_excel(writer, sheet_name='Commits')
     df_pulls.to_excel(writer, sheet_name='Pull Requests')
     df_pull_comments.to_excel(writer, sheet_name='PR Comments')
 




