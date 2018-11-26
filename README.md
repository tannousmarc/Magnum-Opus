# Description

This project should serve as an intermediary layer between users and their data sets.
After providing various data sources (SQL, Key/Value stores, CSV, etc.), the user will be prompted with a search box to query the entirety of their data. Similar entries in the provided data sets will be identified and merged (i.e. concatenate all the provided details of the same person). The user's questions will be parsed into queries applied to the merged data set (i.e. "Which students have worked as TAs for both Functional Programming and Language Engineering over the past 5 years?"). There should be heavy emphasis on developing the UX for viewing/manipulating the results of a query.

# Progress

~~1. Outline project with David before starting any work.
~~2. Identify sample data sets for demo/testing.~~
~~3. Mock-up UI.~~
~~4. Parse questions to queries.~~
~~5. Link front-end to back-end such that it displays the result of a provided question.~~
4. Create adaptor for SQL -> SparQL.
5. Create adaptor for non-relational -> SQL -> SparQL or -> SparQL.
6. MVP. (Release 1)
7. Explore how to derive semantics from unstructured data.
8. Develop algorithm for identifying similar objects.
9. Develop merging procedure based on newly found structure.
10. (Release 2)
11. Provide more data visualization options.


# Credits

Machinalis for quepy.
https://alexn.org/blog/2012/01/16/cosine-similarity-euclidean-distance.html.
