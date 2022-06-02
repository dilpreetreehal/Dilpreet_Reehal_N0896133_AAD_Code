import cv2
# global frame
import os
class Camera():
    def __init__(self,path,projectName):
        self.path=path
        self.projectName=projectName
        self.highestFileNumber = 0

    def openCamera(self):
        cam = cv2.VideoCapture(0)
        cv2.namedWindow("test")
        img_counter = 0
        while True:
            ret, frame = cam.read()
            if not ret:
                print("Can't open application")
                break
            cv2.imshow("test", frame)
            k = cv2.waitKey(1)
            if k % 256 == 27:
                # ESC pressed
                print("Closing Application")
                break
            elif k % 256 == 32:
                # SPACE pressed
                img_name = "WebPhoto_frame_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} Photo Taken".format(img_name))
                img_counter += 1
        cam.release()
        cv2.destroyAllWindows()

    def takePic(self):

        cam = cv2.VideoCapture(0)
        cv2.namedWindow("test")

        ret, frame = cam.read()
        path=self.path + "/Prisms/Images/"

        isExist = os.path.exists(path)

        if isExist == False:
            os.makedirs(path, exist_ok=False)
        else:
            for fileName in os.listdir(path):
                print(fileName)
                if fileName.endswith(".v"):
                    dirFile = fileName.split('.')
                    if(int(dirFile[1])>=int(self.highestFileNumber)):
                        dirNum=int(dirFile[1])
                        self.highestFileNumber=dirNum+1
                        print("high"+str(self.highestFileNumber))


        img_name = self.projectName + ".png".format(self.highestFileNumber)

        cv2.imwrite(self.path + "/Prisms/Images/" + img_name, frame)
        base_file = os.path.splitext(img_name)


        os.rename(self.path + "/Prisms/Images/" + img_name, self.path + "/Prisms/Images/" + base_file[0] +'.'+str(self.highestFileNumber)+ '.v')

        print("Photo Taken")
        # int(self.highestFileNumber)




