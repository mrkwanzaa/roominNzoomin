
class Student:
    # not sure what form surveyValues will come in yet
    def __init__(self, kerb, prefs, surveyValues):
        self.prefs = prefs.copy()
        self.survey = surveyValues
        self.kerb = kerb
    
    def __str__(self):
        return self.kerb