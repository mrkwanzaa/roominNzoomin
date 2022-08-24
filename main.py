from floors import Floor
from students import Student
import pandas as pd
import random

# Checks that at least one floor has room for staple group
def checkForStapleRoom(size, floors):
    for floor in floors.values():
        if floor.openSpots >= size:
            return True
    return False


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
            if floors[floor].openSpots >= student.size:
                floors[floor].addStudent(student)
                break
            # if it is full - check if this student has more compatible survey answers than anyone else
            # This function only returns true for less compatible students
            def filterStudents(currentStudent):
                return (
                    currentStudent.prefs.index(floor) <= idx
                    and currentStudent.checkSurvey(floors[floor])
                    < student.checkSurvey(floors[floor])
                    and checkForStapleRoom(currentStudent.size, floors)
                )

            # Check to see if there are any
            floorStudents = list(
                filter(filterStudents, floors[floor].assignedStudents.copy())
            )
            # Sort any by compatibility
            floorStudents.sort(key=lambda x: x.checkSurvey(floors[floor]))
            if len(floorStudents) > 0:
                # if yes - bump least compatible student out and add this student
                floors[floor].removeStudent(floorStudents[0])
                floors[floor].addStudent(student)
                students.append(floorStudents[0])
                break
        else:
            print(str(student) + " not matched!!")
        i += 1

    # write floors with all matches to .txt
    with open('output.txt', 'a') as f:
        for (key, item) in floors.items():
            f.write(key + ": " + str(item) + "\n")
