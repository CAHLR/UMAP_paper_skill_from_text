# UMAP_paper_skill_from_text
Python code to identify skill from problem text

The code is written in Python3.

Dependencies:-
1) pandas
2) numpy
3) nltk
4) sklearn


There are 16 number of permutations by varying different parameters involved in our experiments. To allow them to run in parallel we have created different python scripts for each of the case located at "Main/BOW/" directory. The random train/test split is performed using the problemIDs and saved at 'ProblemTrainSplit' and 'ProblemTestSplit' to compare our model with the skip-gram experiments.

Steps to run:- 

1) Clone the repository.
2) Enter into UMAP_paper_skill_from_text directory
      cd UMAP_paper_skill_from_text directory
3) Make Directory Result and BOW to save the results
      mkdir Result
      cd Result
      mkdir BOW
      cd ..
4) grant permission to bow.sh to make it executable
      chmod +x bow.sh
5) Execute bow.sh
      ./bow.sh
      
Accuracies will be stored in csv file in Result/BOW folder with their parameters. The actual main file that is executes is at Main/BOW/main1 ... Main/BOW/main16
