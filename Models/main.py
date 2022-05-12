import cv2
from PyQt5 import QtWidgets
from loginPageUI import Ui_Dialog
from Models.databaseClass import Database
import sys


def myfunc():
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




# if __name__ == "__main__":
#
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Dialog()
#     ui.setupUi(Form)
#     Form.show()
#     db = Database()
#     myfunc()
#     sys.exit(app.exec_())