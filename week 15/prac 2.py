def getScores():
    count = int(input("Enter number of students:"))
    scores = []
    for i in range(count):
        score = float(input(f"Enter score for student {i+1}: "))
        scores.append(score)
    return scores

# calls getScores which return a list
classScore = getScores()
highest = max(classScore)
print(f"The highest class score is {highest}")
print(classScore)