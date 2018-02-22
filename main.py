from bow_new import bagOfWords
x = bagOfWords(model_type="NN")
answer = x.predict()
print (answer)


#from singleSkill import KC_analysis
#x = KC_analysis(min_count = [5], repr_type="withoutCorrectness",dataset="2012",split_type="base_sequence")
#answer = x.predict()
#print (answer)
#
