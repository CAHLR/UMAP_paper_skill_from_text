

stemming = [True, False]
with_html = [True, False]
model_type = ["NN", "NB"]
split_type = ["problem", "base_sequence"]

counter = 1
for i in stemming:
    for j in with_html:
        for k in split_type:
            for n in model_type:
                st = """import os, sys\nsys.path.append(os.getcwd())\nfrom bow_new import bagOfWords\nimport pandas as pd\nd = {}\n"""
                st = st + """d["stemming"] = %s\nd["with_html"] = %s\nd["split_type"] = "%s"\nd["model_type"] = "%s"\n""" %(i,j,k,n)
                st = st +"""x = bagOfWords(**d)\nanswer = x.predict()\nfor i,j in d.items():\n\tanswer[i] = [j]*5\ndf = pd.DataFrame(answer)\ndf.to_csv("Result/BOW/bow%d.csv", sep=",", index=False)\nprint (df)\n""" %(counter)
                f = open("main"+str(counter)+".py", "w")
                f.write(st)
                counter += 1

