import pandas as pd
new_path = ""
def train_test_problems(model="BOW_withhtml", st="P"):
    print (st)
    for i in range(5):
        if st == "P":
            l1 = pd.read_csv(new_path+"ProblemTestSplit/test"+str(i+1)+".csv", sep=",",header=None)
            l2 = pd.read_csv(new_path+"ProblemTrainSplit/train"+str(i+1)+".csv", sep=",",header=None)
        elif st == "B":
            l1 = pd.read_csv(new_path+"BaseTestSplit/test"+str(i+1)+".csv", sep=",",header=None)
            l2 = pd.read_csv(new_path+"BaseTrainSplit/train"+str(i+1)+".csv", sep=",",header=None)
        else:
            l1 = pd.read_csv(new_path+"UserIdSplit/test"+str(i+1)+".csv", sep=",",header=None)
            l2 = pd.read_csv(new_path+"UserIdSplit/train"+str(i+1)+".csv", sep=",",header=None)
        if st == "Comp":
            x = pd.read_csv(new_path+"UserIdSplit/"+"withCorrect5"+".csv", sep=",", header=None)
        else:
            x = pd.read_csv(new_path+"TotalProblems/"+model+".csv", sep=",", header=None)
        x = set(list(x[0]))
        l1 = set(list(l1[0]))
        l2 = set(list(l2[0]))
        d1 = x.intersection(l1)
        d2 = x.intersection(l2)
        d1 = d1.difference(d2)
        print (len(d1), len(d2), len(d2.intersection(d1)))
        yield (list(d2), list(d1))
        if st=="Comp":
            break

def train_test(model):
    if model == "PBOWHTML":
        k = train_test_problems(model="BOW_withhtml")
    elif model == "PBOW":
        k = train_test_problems(model="BOW_withouthtml")
    elif model == "BBOWHTML":
        k = train_test_problems(model="BOW_withhtml", st="B")
    elif model == "BBOW":
        k = train_test_problems(model="BOW_withouthtml",st="B")
    elif model == "PC0":
        k = train_test_problems(model="withcorrect_Problem0")
    elif model == "P0":
        k = train_test_problems(model="withoutcorrect_Problem0")
    elif model == "PC5":
        k = train_test_problems(model="withcorrect_Problem5")
    elif model == "P5":
        k = train_test_problems(model="withoutcorrect_Problem5")
    elif model == "BC0":
        k = train_test_problems(model="withcorrect_Problem0",st="B")
    elif model == "B0":
        k = train_test_problems(model="withoutcorrect_Problem0", st="B")
    elif model == "BC5":
        k = train_test_problems(model="withcorrect_Problem5", st="B")
    elif model == "B5":
        k = train_test_problems(model="withoutcorrect_Problem5", st="B")
    elif model == "PC10":
        k = train_test_problems(model="withcorrect_Problem10")
    elif model == "P10":
        k = train_test_problems(model="withoutcorrect_Problem10")
    elif model == "BC10":
        k = train_test_problems(model="withcorrect_Problem10",st="B")
    elif model == "B10":
        k = train_test_problems(model="withoutcorrect_Problem10", st="B")
    elif model == "PC20":
        k = train_test_problems(model="withcorrect_Problem20")
    elif model == "P20":
        k = train_test_problems(model="withoutcorrect_Problem20")
    elif model == "BC20":
        k = train_test_problems(model="withcorrect_Problem20",st="B")
    elif model == "B20":
        k = train_test_problems(model="withoutcorrect_Problem20", st="B")
    elif model == "CompBC20":
        k = train_test_problems(model="withcorrect_Problem20", st="Comp")
    elif model == "CompPC20":
        k = train_test_problems(model="withcorrect_Problem20", st="Comp")
    elif model == "CompPC5":
        k = train_test_problems(model="withcorrect_Problem5", st="Comp")
    else:
        k = 0
    return k

#il = train_test("CompBC20")
#for i in l:
#    print (1)
"""

5 supervised 24635 withCorrectness 86% (can be improved)
5 unsupervised 24635 withCorrectness 56% (can be improved)
0 supervised 50348 withoutCorrectness 82% (cab be improved)
0 unsupervised 50348 withoutCorrectness 45% (can be improved very little)

"""
