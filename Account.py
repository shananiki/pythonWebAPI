class Account:


    def __init__(self, accountName, password):
        self.name = accountName
        self.password = password

    def setName(self, accountName):
        self.name = accountName

    def setName(self, password):
        self.password = password

    def getName(self):
        return self.name

    def getPassword(self):
        return self.password