<h1>PowerBI Data Model</h1>

<h2>Summary 💡</h2>

The PowerBI model allows users to easily and accurately slice and dice data.  It consists of tables that have relationships to one another, and these relationships are key to having a dynamic dashboard and data integrity.  The model was complex to design because I wanted to report on "summary data" coming straight out of GitHub.  This consists of metrics measuring the number of pull requests over time and the number of comments per contributor, as examples.  However, I also wanted to visualize details.  For example, I wanted to create a relationship between specific cases and matching pull requests.   Mixing "summary" and "detail" data and avoiding ambiguity were challenges that I faced when designing this model.  Please read the following sections to see how I solved this problem!  

The BI model consists of nine tables.  These tables include a:

- Set of four tables containing GitHub data extracted with a [Python script](https://github.com/lewisdecarolis19/GithubUtilizationMetrics/blob/main/Get_GitHub_Data.py)
  - Pull Requests, PR Comments, Commits, and Contributors 
- GH Contributions table that merges and appends the aforementioned four tables
  - This table is used to easily visualize the repository summary data
- Cases and Projects table where the data is obtained via an internal dataflow
- Dates table used for analyzing data over time
- Cases/Projects vs Pull Requests table containing all case records along with matching pull request records
  - This is achieved through a left join
  - The purpose of this table is to visualize which cases do not have a related pull request.  Default table visualizations only utilize an inner join
- Repositories table that links GitHub contributions to case products     


<p align="center">
<img src="https://github.com/lewisdecarolis19/images/blob/main/GitHubModel1.png" height="80%" width="80%" alt="Data Model"/>
<br />
<br />
</p>

<h2>Design 🧩</h2>

A significant portion of the model was designed in star schema format.  This structure includes fact tables that contain the primary data for reporting, along with dimension tables that hold attributes related to the fact tables.  The dimension tables are utilized in the dashboard to enable accurate drill-downs and data filtering based on these attributes.

Fact Tables:
- GH Contributions
  - Reports on summary metrics from the GitHub repositories 
  - Pull requests, PR comments, commits, and merges appended into one table
  - A categorical field seperates all of the records by contribution type
- Cases and Projects

Dimension Tables:
- Dates
- Contributors
- Repositories

Transactional tables are also included in the model.  These tables contain the complete, transactional repository data extracted from GitHub using the [Python script](https://github.com/lewisdecarolis19/GithubUtilizationMetrics/blob/main/Get_GitHub_Data.py).  They are not part of the star schema design because ambiguity could otherwise be introduced into the model.

Transaction Tables:
- Pull Requests
- PR Comments
- Commits
- Cases/Projects vs Pull Requests

<p align="center">
<img src="https://github.com/lewisdecarolis19/images/blob/main/GitHubModel2.png" height="80%" width="80%" alt="Data Model Design"/>
<br />
<br />
</p>

<h4>Challenge</h4>

The main challenge in designing this model was enabling it to analyze both "summary" and "transactional" data.  Integrating these two types of reporting into a single model introduced ambiguity.  For instance, the Dates dimension table needed to have a one-to-many relationship with both the Pull Requests and Cases/Projects tables.  This created a "circular flow" in the model, resulting in errors and ambiguity in data filtration.  Similar issues arose when establishing relationships for other transaction tables.

<h4>Solution</h4>




<h2>Table Relationships 🔑</h2>

<p align="center">
<img src="https://github.com/lewisdecarolis19/images/blob/main/GitHubModel3.png" height="80%" width="80%" alt="Table Relationships"/>
<br />
<br />
</p>

<h2>Project Files 📄</h2>

-  [Python Script](https://github.com/lewisdecarolis19/GithubUtilizationMetrics/blob/main/Get_GitHub_Data.py)
-  [Power Query ETL](https://github.com/lewisdecarolis19/GithubUtilizationMetrics/blob/main/Power%20Query%20ETL/README.md)
-  [PowerBI Model](https://github.com/lewisdecarolis19/GithubUtilizationMetrics/blob/main/PowerBI%20Model/README.md)
-  [PowerBI Dashboard](https://github.com/lewisdecarolis19/GithubUtilizationMetrics/tree/main/PowerBI%20Dashboard)
