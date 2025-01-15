<h1>Team Github Utilization and Compliance</h1>

<h2>Objective</h2>
The objective of this project is to assess the effectiveness of utilizing GitHub as the team's code repository and review tool.  The team has established protocols that require the submission of pull requests and subsequent code reviews under specific circumstances.  This analysis aims to compare the expected number of pull requests and internal cases requiring such submissions, against the actual number of pull requests and reviews conducted.  Ultimately, this project seeks to evaluate the team's adherence to the established processes for code repository usage and code review practices.

<h2>Project Questions</h2> 
  
 
  -  How has the team's usage of GitHub changed over time?  What is the trend over the past ___ quarters or years? Is there a reason for this?
  -  Are we utilizing Github as our code review tool as intended, or are we defaulting to other tools and methods?
  -  How does the number of internal cases requiring a code review submission compare to the actual number of pull requests? Which cases didn't have a pull request that should have?
  -  Are there certain types of internal cases that are more susceptible to not receiving a pull request?  Why is this?
  -  How many commits are pushed per pull request, on average? Are we commiting new code after it has been reviewed by the team?
  -  Are there pull requests that have not been reviewed and have no comments on them?  How many comments or reviewers does each pull request receive, on average?
  -  Who is contributing the most to the health of our repositories?  Who is not following our established protocols for code reviews?
  -  Is code actually being merged when finallized?
  -  What type of contributions does the team need to improve? For example, are we good at leaving reviews on code but bad about committing new code after a review?
  -  Is the lack of contribution to the repository because of a training or process gap?  How can we fill this gap and support eachother better as a team?

<h2>Process and Tools</h2>

- A <b><font color="red">Python</font></b> script, developed in <b>Jupyter Notebooks</b>, interacts with the GitHub Rest API to gather repository data in JSON format.  The script handles the default pagination of the API, and nested for loops are used to iterate through 2 repositories and 4 endpoints.
  - Data specifically pertains to commits, pull requests, pull request comments, and contributors.
  - The data is structured into data frames using the <b>Pandas</b> library and then concatenated and appended into a list of finalized data frames.
  - The <b>ExcelWriter</b> function is used to submit each data frame in the list to its own tab in an output spreadsheet.
  - The spreadsheet is pathed locally to a synced Sharepoint folder.  When the script is ran, the file in Sharepoint is replaced with a file containing new data.
  - The Python script is scheduled to run every morning through <b>JupyterLab</b>.
- The spreadsheet is imported into <b>PowerBI</b> to perform the analysis of the project.
  - The raw, unprocessed data is refined and transformed into a suitable format for analysis using <b>PowerQuery</b>.  For example, all the GitHub contributions are appended into a single table.
  - A star schema <b>BI model</b> is built using refined tables, with the GitHub contributions table as the fact table.  Additional “transactional” tables are linked through specific relationships.
  - Internal organizational case and project data are input into the dashboard using dataflows. This data will be used to compare the actual number of pull requests with the estimated number based on the eligible internal cases.
  - <b>Visualizations</b> are created to provide unique insights and identify trends in the data.  Examples of the included visualizations are included in the “Conclusions” section below.
- The developed dashboard is used to optimize team processes, operations, and performance.










<h2>Program walk-through:</h2>

<p align="center">
Launch the utility: <br/>
<img src="https://i.imgur.com/62TgaWL.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Select the disk:  <br/>
<img src="https://i.imgur.com/tcTyMUE.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Enter the number of passes: <br/>
<img src="https://i.imgur.com/nCIbXbg.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Confirm your selection:  <br/>
<img src="https://i.imgur.com/cdFHBiU.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Wait for process to complete (may take some time):  <br/>
<img src="https://i.imgur.com/JL945Ga.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Sanitization complete:  <br/>
<img src="https://i.imgur.com/K71yaM2.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Observe the wiped disk:  <br/>
<img src="https://i.imgur.com/AeZkvFQ.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
