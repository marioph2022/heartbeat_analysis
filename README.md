# Analysis of synthetic heartbeat data
Anomaly detection of synthetic heartbeat data using TDA

This is a short analysis of synthetic heartbeat data using topological data analysis (TDA).  The analysis is done via a set of python programs which use the regular libraries like pandas, numpy and matplotlib to analyze the data plus neurokit2 and tda from giotto. The library neurokit2 is used to create synthetic data and giotto to analyze and find anomalies using topological data analysis.

Topological data analysis is a set of tools with the aim of creating descriptores based on the shape of the data.  The results demoed on the python files use the technique known as persistent homology to compute how the connections between data points behave and the holes created during this connecting process.  Connections are determined by creating circunferences centered at the data points with a radious r that starts from zero and starts growing until all the circunferences intersect to connect the data and create holes.

Programs included in this project:

- x_heartbeat.ipynb - Main program
- x01_tda_diagrams.py - Program to obtain de TDA descriptors
- x02_tda_train_test_split.py - Program to split data
- x03_tda_train_test_model.py - Program to train a model
- x04_tda_distances.py - Program to compare descriptors and find "distances"

Link to installation instructions and python dependencies:

https://github.com/giotto-ai/giotto-tda

While running the main program as is, different synthetic heartbeat data is created so output that shows how similar heartbeats are might be different.  Thie following image is what was created during one run

