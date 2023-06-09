import cv2
import matplotlib.pyplot as plt

fd = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
vid = cv2.VideoCapture(0)
while True:

    flag, img = vid.read()
    if flag:
        # Processing Code
        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = fd.detectMultiscale(img_gray,1.1,5)
        
        # th, img_bw = cv2.threshold(img_gray,100,255,cv2.THRESH_BINARY_INV)
        for x,y,w,h in faces:
        # x,y,w,h = (250,250,100,100)
        # img_cropped = img[y:y+h, x:x+w, :]

        cv2.rectangle(
            img, pt1=(x,y), pt2=(x+w, y+h), color=(0,0,255),
            thickness=8
            )

        cv2.imshow('Preview',img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    else:
        print('NO FRAMES')
        break
vid.release()
cv2.destroyAllWindows()
