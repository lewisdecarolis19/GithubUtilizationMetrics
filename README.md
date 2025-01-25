<h1>Team Github Utilization and Compliance</h1>

<h2>Objective 🎯</h2>
The objective of this project is to assess the effectiveness of utilizing GitHub as the team's code repository and review tool.  The team has established protocols that require the submission of pull requests and subsequent code reviews under specific circumstances.  This analysis aims to compare the expected number of pull requests and internal cases requiring such submissions, against the actual number of pull requests and reviews conducted.  Ultimately, this project seeks to evaluate the team's adherence to the established processes for code repository usage and code review practices.

<h2>Business Questions 🔎</h2> 
  
 
  -  How has the team's usage of GitHub changed over time?  What is the trend over the past ___ quarters or years? Is there a reason for this? 
  -  Are we utilizing Github for code reviews as intended?
  -  How does the number of internal cases requiring a code review submission compare to the actual number of pull requests? Which cases didn't have a pull request that should have?
  -  Are there certain types of internal cases that are more susceptible to not receiving a pull request?  Why is this?
  -  How many commits are pushed per pull request, on average? Are we commiting new code after it has been reviewed by the team?
  -  How many comments or reviewers does each pull request receive, on average?
  -  Who is contributing the most to the health of our repositories?  Who is not following our established protocols for code reviews?
  -  What type of contributions does the team need to improve? For example, are we good at leaving reviews on code but bad about committing new code after a review?
  -  Is the lack of contribution to the repository because of a training or process gap?  How can we fill this gap and support eachother better as a team?

<h2>Solution ⚡️ </h2>

<h2>Process and Tools 🔨 </h2>

1. A [Python script](https://github.com/lewisdecarolis19/GithubUtilizationMetrics/blob/main/Get_GitHub_Data.py), developed in <b>Jupyter Notebooks</b>, interacts with the [GitHub REST API](https://docs.github.com/en/rest?apiVersion=2022-11-28) to gather repository data in JSON format.  The script handles the default pagination of the API, and nested for loops are used to iterate through 2 repositories and 4 endpoints.
    - Data specifically pertains to commits, pull requests, pull request comments, and contributors.
    - The data is structured into data frames using the <b>Pandas</b> library and then concatenated and appended into a list of finalized data frames.
    - The <b>ExcelWriter</b> function is used to submit each data frame in the list to its own tab in an output spreadsheet.
    - The spreadsheet is pathed locally to a synced Sharepoint folder.  When the script is ran, the file in Sharepoint is replaced with a file containing new data.
    - The Python script is scheduled to run every morning through <b>JupyterLab</b>.
2. The spreadsheet is imported into <b>PowerBI</b> to perform the analysis of the project.
    - The raw, unprocessed data is refined and transformed into a suitable format for analysis using <b>PowerQuery</b>.  For example, all the GitHub contributions are appended into a single table.
    - A star schema [PowerBI model](https://github.com/lewisdecarolis19/GithubUtilizationMetrics/tree/main/PowerBI%20Model) is built using refined tables, with the GitHub contributions table as the fact table.  Additional “transactional” tables are linked through specific relationships.
    - Internal organizational case and project data are input into the dashboard using dataflows. This data will be used to compare the actual number of pull requests with the estimated number based on the eligible internal cases.
    - <b>Visualizations</b> are created to provide unique insights and identify trends in the data.  Examples of the included visualizations are included in the “Conclusions” section below.
3. The developed dashboard is used to optimize team processes, operations, and performance.


<h2>Results and Recommendations 🚀</h2>

🚧 In Process 🚧

<h2>Project Files 📄</h2>

-  [Python Script](https://github.com/lewisdecarolis19/GithubUtilizationMetrics/blob/main/Get_GitHub_Data.py)
-  [Power Query ETL](https://github.com/lewisdecarolis19/GithubUtilizationMetrics/blob/main/Power%20Query%20ETL/README.md)
-  [PowerBI Model](https://github.com/lewisdecarolis19/GithubUtilizationMetrics/blob/main/PowerBI%20Model/README.md)
-  [PowerBI Dashboard](https://github.com/lewisdecarolis19/GithubUtilizationMetrics/tree/main/PowerBI%20Dashboard)

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
