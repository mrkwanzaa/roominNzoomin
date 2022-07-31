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
        students.append(Student(row['kerb'], prefs, 'test'))
    
    # randomize students ordering
    random.shuffle(students)

    #TODO: add survey values here to modify student rankings

    # Match students - rewriite using resideny algorithm (Gale-Shapely)
    # Staples are considered one student for matching - but remove multiple floor spots
    for student in students:
        for idx in range(len(student.prefs)):
            if idx > 3:
                print(student.kerb + " not able to get top 4 prefs")
            floor = student.prefs[idx]
            if floors[floor].openSpots > 0:
                floors[floor].addStudent(student)
                break

    # print floors with all matches   
    print([key + ": " + str(item) for (key, item) in floors.items()])
            