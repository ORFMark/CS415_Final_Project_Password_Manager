class InfoClass:
    def __init__(self):
        self.user = ""
        self.passwordDict = dict()
        self.numberOfInstances = 0;
    def getUser(self):
        return self.user
    def setUser(self, user):
        self.user = user
    def getPasswords(self):
        return self.passwordDict
    def setPasswords(self, passwordDict):
        self.passwordDict = passwordDict
    def getNumberOfInstances(self):
        return self.numberOfInstances
    def setNumberOfInstances(self, numOfInstances):
        self.numberOfInstances = numOfInstances