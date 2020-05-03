'''
import speech_recognition as sr
r = sr.Recognizer()

harvard = sr.AudioFile('male.wav')
with harvard as source:
    audio = r.record(source)
print(r.recognize_google(audio))
'''




# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
from datetime import datetime

#start_lesson -> clears file, and lesson date
def start_lesson():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    with open('lesson_transcript.txt','w') as f:
        f.write(current_time+'\n')

#write audio transcript to file   
def update_file(speaker,text):
    with open('lesson_transcript.txt','a') as f:
        f.write(speaker+':'+text+'\n')

#get audio transcript of speaker
def recognise():
    speaker = input('Speaker Name: ')
    
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #print("Say something!")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        
        output = r.recognize_google(audio)
        print('\n\nCC: "' + output + '"\n')
        update_file(speaker,output)
        
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

#initialise lesson
start_lesson()

#loop through lesson
while True:
    print('\n\n\n')
    #get CC of speaker
    recognise()
