class InfoClass:
    user = ""
    passwordDict = dict()
    def getUser(self):
        return self.user
    def setUser(self, user):
        self.user = user
    def getPasswords(self):
        return self.passwordDict
    def setPasswords(self, passwordDict):
        self.passwordDict = passwordDict