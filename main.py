from floors import Floor
from students import Student
import pandas as pd
import random
import sys

# Checks that at least one floor has room for staple group
def checkForStapleRoom(size, floors):
    # Checks command line flags to prevent bumping issues
    if '--save-staples' in sys.argv:
        return size < 2
    elif '--no-bump' in sys.argv:
        return False
    for floor in floors.values():
        if floor.openSpots >= size:
            return True
    return False


if __name__ == "__main__":
    floors = {}
    students = []
    print("Creating floor objects")
    # initialize floor and student objects
    floorsDF = pd.read_csv("floors.csv")
    for (idx, row) in floorsDF.iterrows():
        floors[row["name"]] = Floor(row["spots"], {})
    print("Creating student objects")
    studentsDF = pd.read_csv("students.csv")
    for (idx, row) in studentsDF.iterrows():
        prefs = list(floors.keys())
        prefs.sort(key=lambda i: row[list(floors.keys())].get(i))
        students.append(Student(row["kerb"], prefs))

    print("Randomizing student order")
    # randomize students ordering
    random.shuffle(students)

    # Staples are considered one student for matching - but remove multiple floor spots
    print("Sorting...")
    i = 0
    while i < len(students):
        student = students[i]
        # run for each floor in order of preference
        for idx in range(len(student.prefs)):
            floor = student.prefs[idx]
            # if not full - add this student
            if floors[floor].openSpots >= student.size:
                floors[floor].addStudent(student)
                break

            # This function only returns true for less compatible students who
            # ranked the given floor less or equally and have room availible elsewhere
            def filterStudents(currentStudent):
                return (
                    currentStudent.prefs.index(floor) <= idx
                    and currentStudent.checkSurvey(floors[floor])
                    < student.checkSurvey(floors[floor])
                    and checkForStapleRoom(currentStudent.size, floors)
                )
            
            # Filter out more compatible or students who ranked higher
            floorStudents = list(
                filter(filterStudents, floors[floor].assignedStudents.copy())
            )
            # Sort any less compatible by compatibility
            floorStudents.sort(key=lambda x: x.checkSurvey(floors[floor]))

            bumpedSize = 0
            bumpedStudents = []
            # add students to bumpedStudents until there is room for 
            # current or we run out of bumpable students
            while (bumpedSize < student.size and len(floorStudents) > 0):
                removedStudent = floorStudents.pop(0)
                bumpedSize += removedStudent.size
                bumpedStudents.append(removedStudent)
            
            # Only if we successfully bumped enough do we actually move them around
            if bumpedSize >= student.size:
                for removedStudent in bumpedStudents:
                    floors[floor].removeStudent(removedStudent)
                floors[floor].addStudent(student)
                students.extend(bumpedStudents)
                break
        else:
            # This should only happen if a staple group is matched absolute last - or we have too many frosh
            print(str(student) + " not matched!!")
        i += 1

    # write floors with all matches to .txt
    print("Writing output")
    with open('output.txt', 'a') as f:
        for (key, item) in floors.items():
            f.write(key + ": " + str(item) + "\n")
        f.write("=====================\n")
    print("Done!")
