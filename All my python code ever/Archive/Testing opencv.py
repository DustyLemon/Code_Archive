import sys
import numpy as np
sys.path.append('C:\Anaconda2\Lib\site-packages')
import cv2


def display_image(image):
    img = cv2.imread(image)                         #'C:\Users\Th\Downloads\Forest.jpg'
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def capture_video():
    cap = cv2.VideoCapture(0)
    print cap.grab()
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('C:\Users\Th\Videos\output.avi',fourcc, 30.0, (640,480))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:

            # write the flipped frame
            out.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def draw_random_image():
    img = np.zeros((512,512,3), np.uint8)
    img = cv2.line(img,(0,0),(511,511),(255,0,0),5)

    while True:
        cv2.imshow('image',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            cv2.destroyAllWindowsq


def