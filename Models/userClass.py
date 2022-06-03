from databaseClass import Database
class User():
    def __init__(self, name, password):
        self.username = name
        self.password = password
        self.loggedIn = False


    def login(self):
        db = Database()
        self.loggedIn=db.loginQuery(self.username,self.password)
        return self.loggedIn

