classifier_type = ["supervised" , "unsupervised"]
optimization_type = ["validation", "variance"]
classification_feature = ["problemid", "basesequenceid"]
split_type = ["problem", "base_sequence"]
repr_type = ["withCorrectness", "withoutCorrectness"]
distance_measure = ["euclidean", "cosine"]
window_size = list(range(100, 110, 20))
vector_size = list(range(160, 165, 32))
counter = 1
min_count = 20

st = """
d["window_size"] = list(range(100, 110, 20))
d["vector_size"] = list(range(160, 165, 32))
d["dataset"] = "2009"
"""
for i in classifier_type:
    
    for j in optimization_type:
        for k in split_type:
            for m in repr_type:
                for n in distance_measure:
                        if i=="supervised":
                            n = "NA"
                        st = """import os, sys, datetime\nnewpath='/research/anant/SkillModel/'\nsys.path.append(newpath)\nfrom singleSkill import KC_analysis\nimport pandas as pd\nd = {}\nd["window_size"] = [5, 10]+list(range(20, 160, 20))\nd["vector_size"] = list(range(64, 256, 32))\nd["dataset"] = "2012"\nd["min_count"] = [%d]\n""" %(min_count)
                        st = st + """d["classifier_type"] = "%s"\nd["optimization_type"] = "%s"\nd["split_type"] = "%s"\nd["distance_measure"] = "%s"\nd["repr_type"] = "%s"\n""" %(i,j,k,n,m)
                        st = st +"""x = KC_analysis(**d)\nanswer = x.predict()\nd["window_size"] = str(d["window_size"][0])+"$$"+str(d["window_size"][-1])\nd["vector_size"] = str(d["vector_size"][0])+"$$"+str(d["vector_size"][-1])\nd["min_count"] = d["min_count"][0]\nfor i,j in d.items():\n\tanswer[i] = [j]*5\ndf = pd.DataFrame(answer)\nif len(sys.argv)==2:\n\tdf.to_csv(newpath+"TempData/"+str(datetime.datetime.now())+".csv", sep=",", index=False)\nelse:\n\tdf.to_csv(newpath+"Accuracy/2012/%d/%d.csv", sep=",", index=False)\nprint (df)\n""" %(min_count, counter)
                        f = open("main"+str(counter)+".py", "w")
                        f.write(st)
                        counter += 1

                        if i=="supervised":
                            break
