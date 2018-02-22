import os, sys, datetime
newpath='/research/anant/SkillModel/'
sys.path.append(newpath)
from singleSkill import KC_analysis
import pandas as pd
d = {}
d["window_size"] = [5, 10]+list(range(20, 160, 20))
d["vector_size"] = list(range(64, 256, 32))
d["dataset"] = "2012"
d["min_count"] = [0]
d["classifier_type"] = "unsupervised"
d["optimization_type"] = "validation"
d["split_type"] = "problem"
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
if len(sys.argv)==2:
	df.to_csv(newpath+"TempData/"+str(datetime.datetime.now())+".csv", sep=",", index=False)
else:
	df.to_csv(newpath+"Accuracy/2012/0/5.csv", sep=",", index=False)
print (df)
