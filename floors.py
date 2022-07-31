
class Floor:
    def __init__(self, openSpots):
        self.openSpots = openSpots
        self.assignedStudents = []

    def addStudent(self, student):
        self.openSpots -= student.size
        self.assignedStudents.append(student)

    def removeStudent(self, student):
        self.assignedStudents.remove(student)
        self.openSpots += student.size

    def __str__(self):
        return str(self.assignedStudents)