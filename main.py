from floors import Floor
from students import Student
import pandas as pd
import random

if __name__ == "__main__":
    floors = {}
    students = []

    # initialize floor and student objects
    floorsDF = pd.read_csv("floors.csv")
    for (idx, row) in floorsDF.iterrows():
        floors[row["name"]] = Floor(row["spots"], row["survey"])
    studentsDF = pd.read_csv("students.csv")
    for (idx, row) in studentsDF.iterrows():
        prefs = list(floors.keys())
        prefs.sort(key=lambda i: row[list(floors.keys())].get(i))
        students.append(Student(row["kerb"], prefs, "test" + str(idx + 1)))

    # randomize students ordering
    random.shuffle(students)

    # Staples are considered one student for matching - but remove multiple floor spots
    i = 0
    while i < len(students):
        student = students[i]
        for idx in range(len(student.prefs)):
            floor = student.prefs[idx]
            # if not full - add this student
            if floors[floor].openSpots > 0:
                floors[floor].addStudent(student)
                break
            # if it is full - check if this student has more compatible survey answers than anyone else
            floorStudents = floors[floor].assignedStudents.copy()
            floorStudents.sort(
                key=lambda x: (len(floors) + x.prefs.index(floor))
                + 0.99 * x.checkSurvey(floors[floor])
            )
            if (
                len(floorStudents) > 0
                and floorStudents[0].prefs.index(floor) <= idx
                and floorStudents[0].checkSurvey(floors[floor])
                < student.checkSurvey(floors[floor])
            ):
                # if yes - bump less compatible student out and add this student
                floors[floor].removeStudent(floorStudents[0])
                floors[floor].addStudent(student)
                students.append(floorStudents[0])
                print(str(floorStudents[0]) + " got bumped")
                break

            if idx > 3:
                print(student.kerb + " not able to get top 4 prefs")
        else:
            print(str(student) + " not matched!!")
        i += 1

    # print floors with all matches
    for (key, item) in floors.items():
        print(key + ": " + str(item))
