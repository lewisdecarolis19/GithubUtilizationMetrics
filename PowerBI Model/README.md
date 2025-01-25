<h1>PowerBI Data Model</h1>

<h2>Summary 💡</h2>

The PowerBI model allows users to easily and accurately slice and dice data.  It consists of tables that have relationships to one another, and these relationships are key to having a dynamic dashboard and data integrity.  The model was complex to design because I wanted to report on "summary data" coming straight out of GitHub.  This consists of metrics measuring the number of pull requests over time and the number of comments per contributor, for example.  However, I also wanted to visualize details.  For example, I wanted to create a relationship between specific cases and matching pull requests.   Mixing "summary" and "detail" data and avoiding redundancies were challenges that I faced when designing this model.  Please read the following sections to see how I solved this problem!  

The PowerBI model consists of nine tables.  These tables include a:

- Set of four tables containing GitHub data imported into PowerBI by the spreadsheet
  - Pull Requests, PR Comments, Commits, and Contributors 
- GH Contributions table that merges appends the aforementioned four tables
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

<p align="center">
<img src="https://github.com/lewisdecarolis19/images/blob/main/GitHubModel2.png" height="80%" width="80%" alt="Data Model Design"/>
<br />
<br />
</p>

<h2>Table Relationships 🔑</h2>

<p align="center">
<img src="https://github.com/lewisdecarolis19/images/blob/main/GitHubModel3.png" height="80%" width="80%" alt="Table Relationships"/>
<br />
<br />
</p>
