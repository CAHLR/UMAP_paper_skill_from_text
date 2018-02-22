

classifier_type = ["supervised" , "unsupervised"]
optimization_type = ["variance", "validation"]
classification_feature = ["problemid", "basesequenceid"]
split_type = ["problem", "base_sequence"]
repr_type = ["withCorrectness", "withoutCorrectness"]
distance_measure = ["euclidean", "cosine"]
window_size = list(range(100, 110, 20))
vector_size = list(range(160, 165, 32))
counter = 0


x = {}
d = {}
st = """
d["window_size"] = list(range(100, 110, 20))
d["vector_size"] = list(range(160, 165, 32))
d["dataset"] = "2009"
"""
counter = 1
for i in classifier_type:
    
    for j in optimization_type:
        for k in split_type:
            for m in repr_type:
                if i=="unsupervised":
                    for n in distance_measure:
                        st = """import os, sys\nsys.path.append(os.getcwd())\nfrom singleSkill import KC_analysis\nimport pandas as pd\nd = {}\nd["window_size"] = list(range(100, 110, 20))\nd["vector_size"] = list(range(160, 165, 32))\nd["dataset"] = "2009"\nd["min_count"] = [0]\n"""
                        st = st + """d["classifier_type"] = "%s"\nd["optimization_type"] = "%s"\nd["split_type"] = "%s"\nd["distance_measure"] = "%s"\nd["repr_type"] = "%s"\n""" %(i,j,k,n,m)
                        st = st +"""x = KC_analysis(**d)\nanswer = x.predict()\nd["window_size"] = str(d["window_size"][0])+"$$"+str(d["window_size"][-1])\nd["vector_size"] = str(d["vector_size"][0])+"$$"+str(d["vector_size"][-1])\nd["min_count"] = d["min_count"][0]\nfor i,j in d.items():\n\tanswer[i] = [j]*5\ndf = pd.DataFrame(answer)\ndf.to_csv("Result/2009/KC%d.csv", sep=",", index=False)\nprint (df)\n""" %(counter)
                        f = open("main"+str(counter)+".py", "w")
                        f.write(st)
                        counter += 1

                else:
                    st = """import os, sys\nsys.path.append(os.getcwd())\nfrom singleSkill import KC_analysis\nimport pandas as pd\nd = {}\nd["window_size"] = list(range(100, 110, 20))\nd["vector_size"] = list(range(160, 165, 32))\nd["dataset"] = "2009"\nd["min_count"] = [0]\n"""
                    st = st + """d["classifier_type"] = "%s"\nd["optimization_type"] = "%s"\nd["split_type"] = "%s"\nd["distance_measure"] = "%s"\nd["repr_type"] = "%s"\n""" %(i,j,k,"NA",m)
                    st = st +"""x = KC_analysis(**d)\nanswer = x.predict()\nd["window_size"] = str(d["window_size"][0])+"$$"+str(d["window_size"][-1])\nd["vector_size"] = str(d["vector_size"][0])+"$$"+str(d["vector_size"][-1])\nd["min_count"] = d["min_count"][0]\nfor i,j in d.items():\n\tanswer[i] = [j]*5\ndf = pd.DataFrame(answer)\ndf.to_csv("Result/2009/KC%d.csv", sep=",", index=False)\nprint (df)\n""" %(counter)
                    f = open("main"+str(counter)+".py", "w")
                    f.write(st)
                    counter += 1
            
                    
