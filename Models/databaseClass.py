import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets


class Database():
    def __init__(self):
        global mydb
        mydb= mysql.connector.connect(
            host="localhost",
            database='PRISM',
            user="admin",
            password="mE9bZfA8fW6W"
        )

        # print(mydb)
        # mycursor = mydb.cursor()
        # mycursor.execute("SELECT * FROM loginTbl")
        # mycursor.fetchall()



    def loginQuery(self,username,password):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM `loginTbl` WHERE `userName`='"+username+"' AND password=PASSWORD('"+password+"')")

        if mycursor.fetchone():
            print("Logged In")
            return True
        else:
            print("Login Failed")

    def sayHi(self):
        print("hi")

    def saveImage(self,projectName,fileName,URL):
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO `imageDB`(`projectName`, `fileName`, `URL`) VALUES ('"+projectName+"','"+fileName+"','"+URL+"')")
        mydb.commit()
        print("sending to db")








