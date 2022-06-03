import cv2
# global frame
import os

from Models.databaseClass import Database


class Camera():

    def __init__(self,path,projectName):
        self.path = path+"/Prisms/Images/"
        self.projectName = projectName
        self.highestFileNumber = 0
        self.fileName = ""



    def openCamera(self):
        cam = cv2.VideoCapture(0)
        cv2.namedWindow("Camera Window")
        while True:
            ret, frame = cam.read()
            if not ret:
                print("Can't open application")
                break
            cv2.imshow("Camera Window", frame)
            k = cv2.waitKey(1)
            if k % 256 == 27:
                # ESC pressed
                print("Closing Application")
                break

        cam.release()
        cv2.destroyAllWindows()



    def saveImage(self):
        db=Database()
        db.sayHi()
        db.saveImage(self.projectName,self.fileName,self.path)
        print(self.projectName)
        print(self.fileName)
        print(self.path)


    def takePic(self):

        cam = cv2.VideoCapture(0)
        ret, frame = cam.read()

        isExist = os.path.exists(self.path)

        if isExist == False:
            os.makedirs(self.path, exist_ok=False)
        else:
            for dirFileName in os.listdir(self.path):
                print(dirFileName)
                if dirFileName.endswith(".v"):
                    dirFile = dirFileName.split('.')
                    if( int(dirFile[1]) >= int(self.highestFileNumber) ):
                        dirNum = int(dirFile[1])
                        self.highestFileNumber = dirNum+1
                        print("high"+str(self.highestFileNumber))


        img_name = self.projectName + ".png".format(self.highestFileNumber)

        cv2.imwrite(self.path + img_name, frame)

        base_file = os.path.splitext(img_name)

        self.fileName = base_file[0] + '.' + str(self.highestFileNumber) + '.v'

        os.rename(self.path + img_name, self.path+self.fileName)

        print("Photo Taken")

        self.saveImage()