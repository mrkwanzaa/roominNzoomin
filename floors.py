
class Floor:
    def __init__(self, openSpots, rankings):
        self.openSpots = openSpots
        self.assignedStudents = []
        self.rankings = rankings

    def addStudent(self, student):
        self.openSpots -= student.size
        self.assignedStudents.append(student)

    def removeStudent(self, student):
        self.assignedStudents.remove(student)
        self.openSpots += student.size

    def __str__(self):
        return str([student.kerb for student in self.assignedStudents])