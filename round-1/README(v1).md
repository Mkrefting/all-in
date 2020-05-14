# All-In
"Making Online Education Accessible for All!"


## Our Code
We have split up 'All-In' into two parts:
1. Live transcription of speaker's voice to text
2. User's display; how it adapts when low bandwidth and how it adapts when no internet connection at all

### How (1) works:

1. Run the python code (through command line works best),
2. Enter speaker's name
3. Speak
4. When speaking is detected to have stopped...,
5. ... the Google Web Speech API translates the audio into text,
6. This text is added to the 'lesson_text.txt' file which represents the lesson text feed

### How (2) works:

* 3 main variables: frame (and audio), bandwidth, live CC
1. Run the 'start_lesson.py' code - this initialises the process of collecting live CCs
(in our case, we collect a random CC from a store of CC's ('random_lesson_transcipt.txt'))
2. With the lesson in progress, 'turn your display on' by running 'main.py'


* If this bandwidth is below 20 Mbps, the bandwidth is recognised as low and a notification appears telling the user that CCs are automatically turning on. The live CCs (as they update into the 'lesson_text.txt' file) are displayed onto the screen.


* If this bandwidth is 0 Mbps / no internet connection is detected, the video/audio stop - from the moment your device has no connection, the CC from the parts of the class you miss is stored on a server - when an internet connection is recognised (bandwidth permitting), the CC the user has missed (due to being offline) is shown on the screen.

* Else if bandwidth is above the threshold point of 20 Mbps (the most effective threshold point will need to be tested for), normal face-to-face video/audio continues.

### Current restrictions
* The user currently sees a 'live video' of themselves
* A random bandwidth between 1 and 70 (Mbps) is generated and displayed
* CCs are updated live to the 'lesson_text.txt' file from a store of audio transcript not from all the teacher / not the students

## SETUP

### Download Requirements (for MacOS X)
```
brew install portaudio
pip install -r requirements.txt
```

### How to run - Display
```
cd Display
python3 start_lesson.py
python3 main.py
```

### How to run - Speech_Recognition
```
cd Speech_Recognition
python3 speech_reco.py
```

## Next steps

To make: Device-Device text streamer on webapp, using video conference streaming server

### Overview:

* Speech-to-text AI on edge
* When speech is detected -> text is sent live to all other devices
* The AI will detect the internet bandwidth
* The text will appear only if somebody has low bandwidth
* If somebody's internet connection is lost and he is reconnected again, the AI will show the person what he missed the last few minutes

### How we will make it:

* Flask
* Zoom API
* Google Web Speach API (for speech recognition)
* OpenCV

### Why: making a standalone web app allows us to test/improve it, as if acting as an add-on to popular video conferencing services

### End goal: integrate with current video streaming services (e.g. Zoom)

### Our resources to continue development:
* [https://rapidapi.com/]
* [https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask]
* [https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps] - how to launch flask app on production server
