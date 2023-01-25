import cv2
import numpy as np
import dlib 
from imutils import face_utils

cap=cv2.VideoCapture(0)
detector=dlib.get_frontal_face_detector()
predictor=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
sleep=0
drowsy=0
active=0
status=""
color=(0,0,0)

def euclideanDistance(a,b):
    return np.linalg.norm(a - b)

def blinked(a,b,c,d,e,f):
    up=euclideanDistance(b,d) + euclideanDistance(c,e)
    down=euclideanDistance(a,f)
    ratio=up/(down*2.0)
    if(ratio>0.25):
        return 2
    elif(ratio<=0.25 and ratio>0.21):
        return 1
    else:
        return 0

