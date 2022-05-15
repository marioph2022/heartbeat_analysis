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

![heartbeat_synthetic_data](https://user-images.githubusercontent.com/98497219/168491776-5dd9a12a-4fef-4c92-beb1-e015b94efec8.jpg)

This example was selected because it is obvious that the third heartbeat is the one with a bigger difference in comparison to the rest of the hearbeats and this difference was detected and measured using TDA distances that are displayed as follows.

![descriptor_distance](https://user-images.githubusercontent.com/98497219/168492179-7ea91e27-6394-4049-992b-c4d60fa99707.jpg)

**Explanation/Description about how PH works in this particular case**

- There are 21 synthetic heartbeats displayed in first plot
- Each synthetic heartbeat is converted to a descriptor (numeric representation of the heartbeats)
- Descriptors are compared using special distances (Landscape, Betti ... and more)
- Distances between the descriptors are summed up plotted on the bars graphs
- There are 21 bars in each of the six distance graphs that tells how different are heartbeats while comparing them to each other

It is up to us depending on the data to define a threshold and say when a difference is "too big" to classify the data as an anomaly.  This can be two standard deviations or something meaninful that allows us to classify data correctly depending on the context of the problem:
