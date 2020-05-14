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
    if counter == 100:
        print('[INFO] Testing Internet Bandwidth...')
        counter = 0
        return True
    if counter % 10 == 0:
        print('[INFO]' + str(100 - counter))
    return False

def add_bandwidth(frame):
    (h,w,d) = frame.shape
    posx = int(round(w * 0.7))
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
    cv2.rectangle(frame, (posx-10, posy-37), (posx+1050, posy+14), (10, 10, 10), -1)
    cv2.putText(frame, cc, (posx, posy), 
	cv2.FONT_HERSHEY_SIMPLEX, 1.2, (200,200,200), 2)

#demo version - will not adjust...
def add_missed_text(frame):
    (h,w,d) = frame.shape
    posx = int(round(w * 0.1))
    posy = int(round(h * 0.9))
    cv2.rectangle(frame, (posx-10, posy-37), (posx+1050, posy+14), (10, 10, 10), -1)
    cv2.rectangle(frame, (posx-10, posy-87), (posx+1050, posy-36), (10, 10, 10), -1)
    cv2.rectangle(frame, (posx-10, posy-137), (posx+1050, posy-86), (10, 10, 10), -1)
    cv2.putText(frame, 'Max: What is the answer?', (posx, posy), 
	cv2.FONT_HERSHEY_SIMPLEX, 1.2, (200,200,200), 2)
    cv2.putText(frame, 'Teacher: Good question, Henry VIII', (posx, posy-50), 
	cv2.FONT_HERSHEY_SIMPLEX, 1.2, (200,200,200), 2)
    cv2.putText(frame, "Suhaas: What is the world's smallest country?", (posx, posy-100), 
	cv2.FONT_HERSHEY_SIMPLEX, 1.2, (200,200,200), 2)   
    
def make_pixelated():
    global frame
    height, width = frame.shape[:2]
    w, h = int(round(width/5)), int(round(height/5))
    temp = cv2.resize(frame, (w, h), interpolation=cv2.INTER_LINEAR)
    frame = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

def add_no_connection():
    global frame
    temp = np.zeros_like(frame)
    frame = temp
    height,width = frame.shape[:2]
    posx = (int(round(width/4)))+50
    posy = (int(round(height/2)))
    cv2.putText(frame, 'No Internet Connection',(posx,posy), 
	cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,0,255), 3)

#counter for regular wifi strength tests
counter = 39
show_cc = False
time_since_start = 6
bandwidth = 100
no_connection = False
show_missed_text = False
time_show_missed_text = 150

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    #check bandwidth every 100 frames
    if time_to_test_bandwidth():
        bandwidth = get_bandwidth()
        if bandwidth == 0:
            no_connection = True
            show_cc = False
            show_missed_text = True
        elif bandwidth < 25:
            no_connection = False
            show_cc = True
        else:
            no_connection = False
            show_cc = False
    
    if show_cc and not no_connection:
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
        cv2.waitKey(200)
    
    #if no_connection
    if no_connection:
        add_no_connection()
        
    #connection back on but havent yet shown words
    if not no_connection and show_missed_text:
        add_missed_text(frame)
        time_show_missed_text -= 1
        if time_show_missed_text == 0:
            show_missed_text = False
            time_show_missed_text = 100
        
    #always show bandwidth
    add_bandwidth(frame)
    
    # Display the resulting frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
