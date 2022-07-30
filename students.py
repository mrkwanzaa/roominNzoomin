
class Student:
    # not sure what form surveyValues will come in yet
    def __init__(self, kerb, prefsDict, surveyValues):
        self.prefs = prefsDict.copy()
        self.survey = surveyValues
        self.kerb = kerb
    
    def __str__(self):
        return self.kerb