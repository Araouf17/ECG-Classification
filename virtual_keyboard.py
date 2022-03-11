import cv2
import numpy as np
#import dlib
from math import hypot
from time import sleep

cap = cv2.VideoCapture(1)
board = np.zeros((500, 500), np.uint8)
board[:] = 255

#detector = dlib.get_frontal_face_detector()
#predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Keyboard settings
keyboard = np.zeros((400, 1000, 3), np.uint8)
keys_set_1 = {0: "Q", 1: "W", 2: "E", 3: "R", 4: "T", 5: "U", 6: "I", 7: "O", 8: "P",
              9: "A", 10: "S", 11: "D", 12: "F", 13: "G", 14: "H", 15: "J", 16:"K", 17:"L",
              18: "Z", 19: "X", 20: "C", 21:"V", 22:"B", 23: "N",24:"M"}

def letter(letter_index, text, letter_light):
    # Keys
    if letter_index == 0:
        x = 0
        y = 0
    elif letter_index == 1:
        x = 100
        y = 0
    elif letter_index == 2:
        x = 200
        y = 0
    elif letter_index == 3:
        x = 300
        y = 0
    elif letter_index == 4:
        x = 400
        y = 0
    elif letter_index == 5:
        x = 500
        y = 0
    elif letter_index == 6:
        x = 600
        y = 0
    elif letter_index == 7:
        x = 700
        y = 0
    elif letter_index == 8:
        x = 800
        y = 0
    elif letter_index == 9:
        x = 0
        y = 100
    elif letter_index == 10:
        x = 100
        y = 100
    elif letter_index == 11:
        x = 200
        y = 100
    elif letter_index == 12:
        x = 300
        y = 100
    elif letter_index == 13:
        x = 400
        y = 100
    elif letter_index == 14:
        x = 500
        y = 100
    elif letter_index == 15:
        x = 600
        y = 100
    elif letter_index == 16:
        x = 700
        y = 100
    elif letter_index == 17:
        x = 800
        y = 100
    elif letter_index == 18:
        x = 100
        y = 200
    elif letter_index == 19:
        x = 200
        y = 200
    elif letter_index == 20:
        x = 300
        y = 200
    elif letter_index == 21:
        x = 400
        y = 200
    elif letter_index == 22:
        x = 500
        y = 200
    elif letter_index == 23:
        x = 600
        y = 200
    elif letter_index == 24:
        x = 700
        y = 200
    width = 100
    height = 100
    th = 3 # thickness
    if letter_light is True:
        cv2.rectangle(keyboard, (x + th, y + th), (x + width - th, y + height - th), (255, 255, ), -1)
    else:
        cv2.rectangle(keyboard, (x + th, y + th), (x + width - th, y + height - th), (255, 0, 0), th)

    # Text settings
    font_letter = cv2.FONT_HERSHEY_PLAIN
    font_scale = 7
    font_th = 4
    text_size = cv2.getTextSize(text, font_letter, font_scale, font_th)[0]
    width_text, height_text = text_size[0], text_size[1]
    text_x = int((width - width_text) / 2) + x
    text_y = int((height + height_text) / 2) + y
    cv2.putText(keyboard, text, (text_x, text_y), font_letter, font_scale, (255, 0, 0), font_th)




def midpoint(p1 ,p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

font = cv2.FONT_HERSHEY_PLAIN


# Counters
frames = 0
letter_index = 0
blinking_frames = 0
text = ""

while True:
    _, frame = cap.read()
   
    keyboard[:] = (0, 0, 0)
    frames += 1
    new_frame = np.zeros((500, 500, 3), np.uint8)
    

    active_letter = keys_set_1[letter_index]

 
        

    # Letters
    if frames == 24:
        letter_index += 1
        frames = 0
    if letter_index == 24:
        letter_index = 0


    for i in range(24):
        if i == letter_index:
            light = True
        else:
            light = False
        letter(i, keys_set_1[i], light)

    cv2.putText(board, text, (10, 100), font, 4, 0, 3)


    #cv2.imshow("Frame", frame)
    #cv2.imshow("New frame", new_frame)
    cv2.imshow("Virtual keyboard", keyboard)
    cv2.imshow("Board", board)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
