import pandas as pd
x = pd.read_csv("withCorrect20.csv", sep=",", header=None)
x1 = pd.read_csv("train1.csv", sep=",", header=None)
x2 = pd.read_csv("test1.csv", sep=",", header=None)
x = (set(list(x[0])))
x1 =(set(list(x1[0])))
x2 = (set(list(x2[0])))
print (len(x.intersection(x1)), len(x.intersection(x2)))
