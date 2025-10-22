def addStudent(name, dict):
    score = float(input(f"Enter score for {name}: "))
    dict[name]=score
    # No need to return dict as it is pass by ref

results = {'JANE':88.8, "JOHN":66.6}
addStudent( "JIMMY", results)
print('Dictionary is updated as below:')
print(results)