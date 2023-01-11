from Account import *
import json
from DatabaseHandler import *

class AccountHandler:


    def __init__(self):
        self.accounts = []
        self.dbh = DatabaseHandler()


    def getDays(self, userid):
        return self.dbh.getDays(userid)

    def updateDays(self, userid, days):
        if self.dbh.updateDays(userid, days):
            return True
        else:
            return False


    def addAccountSQL(self, account):
        self.accounts.append(account)
        self.dbh.addUser(account.getName(), account.getPassword())

    def addAccount(self, account):
        self.accounts.append(account)
        self.account_ds['username'] = account.getName()
        self.account_ds['password'] = account.getPassword()
        self.accounts.append(self.account_ds)

    def printAccounts(self):
        for acc in self.accounts:
            print(acc.getName())


    def checkAccount(self, account):
        found = False
        for acc in self.accounts:
            if acc.getName() == account.getName():
                print("Account {0} was found.".format(account.getName()))
                found = True
        if found:
            return True
        else:
            return False