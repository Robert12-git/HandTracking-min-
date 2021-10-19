from sre_constants import FAILURE, SUCCESS

#opencv import
import cv2
#mediapipe import for hands recognition
import mediapipe as mp
import time
import math

val = int (input ("Enter number of seconds program should run: "))
print (val)

# Start video capture to have data to analyze
cap = cv2.VideoCapture (0)

# Save inital time of program
begin = time.time ()

# Initialize moduls to search for hands and draw if found
mpHands = mp.solutions.mediapipe.python.solutions.hands
hands = mpHands.Hands (False, 4, 0.5, 0.5)
mpDraw = mp.solutions.mediapipe.python.solutions.drawing_utils

condition = True

while condition:
    # Frame read successfully, convert to RGB colors
    SUCCESS, img = cap.read ()
    imgRGB = cv2.cvtColor (img, cv2.COLOR_BGR2RGB)

    # Process image in hands module to start drawing frame by frame
    results = hands.process (imgRGB)
    
    # If hand landmark found, print on image    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks (img, handLms, mpHands.HAND_CONNECTIONS)

    # Condition to stop program, user can choose how many seconds to run program
    hereNow = time.time ()
    # print (math.floor (hereNow - begin) + " " + val)
    if (math.floor (hereNow - begin) == val):
        break

    # Show what camera is recording frame by frame
    cv2.imshow ("Image", img)
    # 1ms second delay to create video 
    cv2.waitKey (1)