import numpy as np
import cv2
import random
from random import randint

cap = cv2.VideoCapture(0)

#get strength of user's wifi
def get_bandwidth():
    return randint(1,70)

#check if time to test wifi strength
def time_to_test_bandwidth():
    global counter
    counter += 1
    if counter == 30:
        print('[INFO] Testing Internet Bandwidth...')
        counter = 0
        return True
    if counter % 10 == 0:
        print('[INFO]' + str(100 - counter))
    return False

def add_bandwidth(frame):
    (h,w,d) = frame.shape
    posx = int(round(w * 0.75))
    posy = int(round(h * 0.05))
    text = 'Internet Bandwidth: ' + str(bandwidth) + ' Mbps'
    if bandwidth >= 20:
        cv2.putText(frame, text, (posx, posy),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (80,80,80), 2)
    else:
        cv2.putText(frame, text, (posx, posy),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
    
#put warning message on user's screen that CC is about to start
def start_cc(frame):
    (h,w,d) = frame.shape
    posx = int(round(w * 0.05))
    posy = int(round(h * 0.1))
    posy2 = posx + 60
    notification_l1 = 'Low Internet Bandwidth,'
    notification_l2 = 'Turning CC On'
    cv2.putText(frame, notification_l1, (posx, posy), 
	cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,255), 3)
    cv2.putText(frame, notification_l2, (posx, posy2), 
	cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,255), 3)

#get cc from live lesson_transcript (i.e. the last sentence said)
def get_cc():
    with open('lesson_transcript.txt','r') as f:
        data = f.readlines()
    lines = []
    for line in data:
        lines.append(line.rstrip())
    #return the last comment/line said in the lesson transcript
    line = lines[-1].split(':')
    speaker,speech = line[0],line[1]
    cc = speaker + ': ' + speech
    return cc


#put cc onto screen
def add_cc(frame,cc):
    (h,w,d) = frame.shape
    posx = int(round(w * 0.1))
    posy = int(round(h * 0.9))
    cv2.putText(frame, cc, (posx, posy), 
	cv2.FONT_HERSHEY_SIMPLEX, 1.2, (80,80,80), 3)


def make_pixelated():
    global frame
    height, width = frame.shape[:2]
    w, h = int(round(width/4)), int(round(height/4))
    temp = cv2.resize(frame, (w, h), interpolation=cv2.INTER_LINEAR)
    frame = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

#counter for regular wifi strength tests
counter = 29
show_cc = False
time_since_start = 6
bandwidth = 100

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()


    #check bandwidth every 100 frames
    if time_to_test_bandwidth():
        bandwidth = get_bandwidth()
        if bandwidth < 20:
            show_cc = True
        else:
            show_cc = False
    
    if show_cc:
        make_pixelated()
        #get CC
        cc = get_cc() 
        #add CC
        add_cc(frame,cc)
        #show 'show cc' notification for first 10 frames
        time_since_start -= 1
        if time_since_start != 0:
            start_cc(frame)
        else:
            time_since_start = 6
    
        #apply adjustments to make look bad quality video
        cv2.waitKey(400)

    #always show bandwidth
    add_bandwidth(frame)
    
    # Display the resulting frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
