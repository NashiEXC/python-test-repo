# code the function addStduent
def addStduent(name, dict):
    dict[name]={}
    a1= float(input(f"enter attempt1 for {name}"))
# code the function getGrade
# it returns the final grade
def getGrade(score):

# code the function getFinalscore
# it returns the final score
def getFinalscore(name, dict):

# 2 attempts are stored in dictionary
# highest attempt will be the finalScore
results = {
'jane': {'attempt1':75.5, 'attempt2':80.5},
'john': {'attempt1':68.5, 'attempt2':60.5}
}

# calls to add in 2 attempts for jimmy
addStduent('jimmy',results)
# calls getFinalscore to get final score
# calls disdplayFinalGrade to display grade