import sqlite3


class DatabaseHandler:


    def __init__(self):
        self.db_file = "database.db"
        self.connection = sqlite3.connect("database.db", check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.isOpen = True

    def addUser(self, username, password):
        if self.cursor is not None and self.isOpen:
            self.cursor.execute('''INSERT INTO users(username, password) VALUES ("{0}", "{1}")'''.format(username, password))
            self.connection.commit()

    def printUsers(self):
        if self.cursor is not None and self.isOpen:
            for row in self.cursor.execute("SELECT * FROM users"):
                print(row)

    def openDatabase(self):
        if not self.isOpen:
            self.connection = sqlite3.connect("database.db", check_same_thread=False)
            self.isOpen = True

    def closeDatabase(self):
        self.connection.close()
        self.isOpen = False

    def updateDays(self, userid, days):
        if self.cursor is not None and self.isOpen:
            if self.getDays(userid) >= 1:
                self.cursor.execute('''UPDATE userDays SET days = {0} WHERE userID = {1}'''.format(days, userid))
                self.connection.commit()
                return True
        else:
            return False


    def getDays(self, userid):
        if self.cursor is not None and self.isOpen:
            self.cursor.execute("SELECT days FROM userDays WHERE userID = ?", (userid,))
            row = self.cursor.fetchone()
            return row[0] if row is not None else 0

