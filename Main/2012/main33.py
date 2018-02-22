import os, sys
sys.path.append(os.getcwd())
from VarsingleSkill import KC_analysis
import pandas as pd
d = {}
d["window_size"] = [5, 10]+list(range(20, 160, 20))
d["vector_size"] = list(range(64, 256, 32))
d["dataset"] = "2012"
d["min_count"] = [10]
d["classifier_type"] = "unsupervised"
d["optimization_type"] = "variance"
d["split_type"] = "base_sequence"
d["distance_measure"] = "euclidean"
d["repr_type"] = "withCorrectness"
x = KC_analysis(**d)
answer = x.predict()
d["window_size"] = str(d["window_size"][0])+"$$"+str(d["window_size"][-1])
d["vector_size"] = str(d["vector_size"][0])+"$$"+str(d["vector_size"][-1])
d["min_count"] = d["min_count"][0]
for i,j in d.items():
	answer[i] = [j]*5
df = pd.DataFrame(answer)
df.to_csv("Result/2012/KC33.csv", sep=",", index=False)
print (df)
