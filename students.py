
class Student:
    # not sure what form surveyValues will come in yet
    def __init__(self, kerb, prefs, surveyValues, size = 1):
        self.prefs = prefs.copy()
        self.survey = surveyValues
        self.kerb = kerb
        self.size = size
    
    #prefs and survey must be the same for all staple members
    def addStaple(self, kerb):
        self.size += 1
        self.kerb = self.kerb + ', ' + kerb

    def __str__(self):
        return self.kerb