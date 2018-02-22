####---------------------------####
#### Created By: Anant Dadu    ####
####                           ####
####                           ####
####                           ####
####---------------------------####

import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

from trainTest import train_test

from nltk.stem.snowball import EnglishStemmer
from nltk.corpus import stopwords as sw

class bagOfWords:

    def __init__(self, stemming=True, stop_words=False, with_html=False, model_type="NB", split_type="problem"):

        self.stemming = stemming
        self.stop_words = stop_words
        self.with_html = with_html
        self.model_type = model_type
        self.split_type = split_type
        st = ""
        if self.split_type == "problem":
            st = st + "P"
        else:
            st = st + "B"

        st = st + "BOW"

        if with_html:
            st = st + "HTML"
            self.load_data = pd.read_csv("Datasets/assistments2012_problem_id_text.csv", sep=",")
        else:
            self.load_data = pd.read_csv("Datasets/assistments2012_problem_id_text_no_html.csv", sep=",")
        self.st = st

    # function for stemming or removing stopwords
    def stemmed_words(self, doc):

        analyzer = CountVectorizer().build_analyzer()
        stemmed_list = [w for w in analyzer(doc)]

        # stemming is performed on the words
        if self.stemming:
            stemmer = EnglishStemmer()
            stemmed_list = [stemmer.stem(w) for w in analyzer(doc)]

        # removal of stop words
        if self.stop_words:
            stemmed_list = [i for i in stemmed_list if i not in list(set(sw.words('english')))]
        return stemmed_list

    # accuracy is measured using training set and test set
    def analysis(self, X_train, X_test, Y_train, Y_test, classifier):
       	pids = list(Y_test["problem_id"])
        X_train = list(X_train["body"])
        X_test = list(X_test["body"])
        Y_train = list(Y_train["skill"])
        Y_test = list(Y_test["skill"])
        print (len(pids), len(X_train), len(X_test), len(Y_train), len(Y_test))
        
        # CountVectorizer removes the stop words or do the stemming
        # and generate the sparse matrix of bag of words
        stem_vectorizer = CountVectorizer(analyzer=self.stemmed_words)
        X_train_counts = stem_vectorizer.fit_transform(X_train)

        # term frequency and inverse document frequency
        # term frequency means that the frequency of each word
        # and inverse document frequency means that the words that
        # occur very frequently are given less weight than to the
        # words that rarely occur
        tfidf_transformer = TfidfTransformer()
        X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
        if classifier == "NB":
            clf = MultinomialNB().fit(X_train_tfidf, Y_train)
        elif classifier == "SVM":
            clf = SVC(probability=False).fit(X_train_tfidf, Y_train)
        else:
            clf = MLPClassifier().fit(X_train_tfidf, Y_train)

        # same model of CountVectorizer and TfIdf is applied to the
        # test set and rank of each predicted output is calculated
        X_test_counts = stem_vectorizer.transform(X_test)
        X_test_tfidf = tfidf_transformer.transform(X_test_counts)

        diff_skills = clf.classes_
        answer = list(clf.predict(X_test_tfidf))
        predicted_probab = clf.predict_proba(X_test_tfidf)
        d0 = {}
        d0["problem_id"] = pids
        d0["actual_skill"] = list(Y_test)
        d0["predicted_skill"] = list(answer)
        total = 0
        correct1 = 0
        correct5 = 0
        correct10 = 0
        rank = []
        for i in range(len(answer)):
            temp = self.accuracy_varients(answer[i], Y_test[i], predicted_probab[i], diff_skills)
            rank.append(temp)
            if temp <= 1:
                correct1 += 1
                correct5 += 1
                correct10 += 1
            elif temp <= 5:
                correct5 += 1
                correct10 += 1
            elif temp <= 10:
                correct10 += 1
            total += 1
        print ("Accuracy_Top_1", float(correct1)/float(total))
        print ("Accuracy_Top_5", float(correct5)/float(total))
        print ("Accuracy_Top_10", float(correct10)/float(total))
        self.Accuracy["Top1"].append(float(correct1)/float(total))
        self.Accuracy["Top5"].append(float(correct5)/float(total))
        self.Accuracy["Top10"].append(float(correct10)/float(total))
        self.Accuracy["Rank"].append(np.median(rank))
        self.Accuracy["NoTrainSamples"].append(len(X_train))
        self.Accuracy["NoTestSamples"].append(len(X_test))

    # split the data into training and test after generating
    # skill_name from problem id and use 5 fold cv
    def split_data(self):

        data = self.load_data
        data_pro_skill = pd.read_csv("Datasets/problem_skill.csv", sep=",")
        problem_train = pd.read_csv("Datasets/2012ProblemTrainingSet.csv", sep=",")

        # problem ids in training skill
        prob_train = list(map(str, list(problem_train["problem_id"])))
        d = dict(zip(data_pro_skill["problem_id"].map(str), data_pro_skill["skill"].map(str)))
        data = data.dropna()
        d1 = dict(zip(data["problem_id"].map(str), data["body"].map(str)))
        Y = []
        X = []
        x = []
        problem_id = []
        c = 0
        for i in prob_train:
            try:
                X.append(d1[i])
                Y.append(d[i])
                problem_id.append(i)
            except:
                c += 1
                x.append(i)
                # 50348 total samples and 50339 after removing missing values
                continue
        print (c)

        Y = pd.DataFrame({"skill": Y, "problem_id":problem_id})
        X = pd.DataFrame({"body": X, "problem_id":problem_id})
        fin = list(X["body"])
        from string import digits, punctuation
        remove_set = digits + punctuation
        words = {word.lower().strip(remove_set) for line in fin for word in line.rsplit(",",1)[0].split()}
        self.Accuracy = {}
        self.Accuracy["Top1"] = []
        self.Accuracy["Top5"] = []
        self.Accuracy["Top10"] = []
        self.Accuracy["Rank"] = []
        self.Accuracy["NoTrainSamples"] = []
        self.Accuracy["NoTestSamples"] = []
    	
    	# problems in training and testing data 
        kf = train_test(self.st)
        for i, j in kf:
            training = list(map(str, list(problem_id)))
            testing = list(map(str, list(problem_id)))
            X_train = X[X["problem_id"].isin(training)]
            X_test = X[X["problem_id"].isin(testing)]
            Y_train = Y[Y["problem_id"].isin(training)]
            Y_test = Y[Y["problem_id"].isin(testing)]

            # print (len(set(list(Y_test['skill']))))
            # print (len(set(list(X_test['problem_id']))))
            # print (len(set(list(Y_train['skill']))))
            # print (len(set(list(X_train['problem_id']))))
            self.analysis(X_train, X_test, Y_train, Y_test, self.model_type)


    # returns the rank of the output
    def accuracy_varients(self, output, correct_skill, prob_list, diff_skills):

        temp_prob = np.sort(prob_list)[::-1]
        try:
            index_output = np.where(diff_skills==correct_skill)[0][0]
            rank = np.where(temp_prob==prob_list[index_output])[0][0]
        except:
            return 10000000000
        return rank+1

    def predict(self):
        self.split_data()
        return self.Accuracy
"""
x = bagOfWords(with_html=True)
x.predict()
"""
