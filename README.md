# Instructions

Inside the client folder you'll find the frontend. Navigate to that directory and run:

`npm install`

To launch the frontend after installing the required packages, run:

`npm run serve`

Inside the nlpengine folder you'll find the server. Use pip to install any missing dependencies.

To launch the server, run:

`python server.py`

# Description

This project should serve as an intermediary layer between users and their data sets.
After providing various data sources (SQL, Key/Value stores, CSV, etc.), the user will be prompted with a search box to query the entirety of their data. Similar entries in the provided data sets will be identified and merged (i.e. concatenate all the provided details of the same person). The user's questions will be parsed into queries applied to the merged data set (i.e. "Which students have worked as TAs for both Functional Programming and Language Engineering over the past 5 years?"). There should be heavy emphasis on developing the UX for viewing/manipulating the results of a query.

# Progress

1.~~Outline project with David before starting any work.~~

2.~~Identify sample data sets for demo/testing.~~

3.~~Mock-up UI.~~

4.~~Parse questions to queries.~~

5.~~Link front-end to back-end such that it displays the result of a provided question.~~

  5.a)Show originating source of response (name of database?).
  
  5.b)Show parsed query from question.

6.Create adaptor for SQL -> SparQL.

7.Create adaptor for non-relational -> SQL -> SparQL or -> SparQL.

8.MVP. (Release 1)

9.Explore how to derive semantics from unstructured data.

10.Develop algorithm for identifying similar objects.

11.Develop merging procedure based on newly found structure.

12.(Release 2)

13.Provide more data visualization options.

14.Add ability to select data sets you're querying from a list of data sets you have access to. (i.e. dbpedia for everyone, organisation-specific sets for employees only)




# Credits

Machinalis for quepy.

https://alexn.org/blog/2012/01/16/cosine-similarity-euclidean-distance.html.
