import pandas as pd
data = pd.read_csv('withcorrect_Problem5.csv', sep=",", header=None)
data1 = pd.read_csv('BOW_withhtml.csv', sep=",", header=None)
x = set(list(data[0]))
x1 = set(list(data1[0]))
print (len(x))
print (len(x1))
print (len(x.intersection(x1)))
