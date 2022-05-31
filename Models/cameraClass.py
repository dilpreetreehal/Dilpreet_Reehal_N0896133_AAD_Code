import cv2
# global frame

class Camera():

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
        img_counter = 0
        ret, frame = cam.read()
        img_name = "Dilprs.png".format(img_counter)
        cv2.imwrite("/Users/Dilpreet/Prism/Prisms/Images/"+img_name, frame)
        print("{} Photo Taken".format(img_name))
        img_counter += 1