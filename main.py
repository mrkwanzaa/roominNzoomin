from floors import Floor
from students import Student
import pandas as pd
import random

if __name__ == "__main__":
    floors = {}
    students = []

    # initialize floor and student objects
    floorsDF = pd.read_csv('floors.csv')
    for (idx, row) in floorsDF.iterrows():
        floors[row['name']] = Floor(row['spots'])
    studentsDF = pd.read_csv('students.csv')
    for (idx, row) in studentsDF.iterrows():
        prefs = list(floors.keys())
        prefs.sort(key= lambda i: row[list(floors.keys())].get(i))
        print(prefs)
        students.append(Student(row['kerb'], prefs, 'test'))
    
    # randomize students ordering
    random.shuffle(students)

    #TODO: add survey values here to modify student rankings

