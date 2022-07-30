from floors import Floor
from students import Student
import pandas as pd

if __name__ == "__main__":
    floorsDF = pd.read_csv('floors.csv')
    floors = {}
    for (idx, row) in floorsDF.iterrows():
        floors[row['name']] = Floor(row['spots'])
    studentsDF = pd.read_csv('students.csv')
    students = []
    for (idx, row) in studentsDF.iterrows():
        prefsDict = dict(row[list(floors.keys())])
        students.append(Student(row['kerb'], prefsDict, 'test'))
        