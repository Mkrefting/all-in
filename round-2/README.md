# All-In
"Making Online Education Accessible for All!"


### Our Code
* Node.js server
* Socket.io manages real time web socket connections

### How All-In currently works:

1. Run the server (as below)
2. Create private room or join private room
3. Enter your name
4. Press the mic, speak, send
5. All members of the private room can see your speech transcript

### Setup for MacOS X
```
git clone https://github.com/Mkrefting/all-in.git
cd Downloads/all-in/round2
brew install node
npm init
npm install dependencies

```
* Change round2/public/script.js line 1: const socket = io('http://your-local-ip:8080'), where 'your-local-ip' is your private IP address
* To allow development server to access your microphone on chrome:
  * Search 'chrome://flags/#unsafely-treat-insecure-origin-as-secure'
  * Find and enable 'Insecure origins treated as secure'
  * Add the IP address and port that you want to ignore the secure origin policy for (e.g. '192.168.1.xyz:8080'
  * Restart chrome

### Running the local server
```
cd Downloads/all-in/round2
node app.js
```
* Anyone in your LAN can now access the website

### Next Steps - Tech Features:
* Automatic speech recognition when voice is detected (no mic button) -> automatically send transcript (no send button)
* Mute button (useful for students)
* Username and Password for private room login
* Use a database (e.g. Firebase) to store audio transcript - past audio transcript can be sent to students even after complete WiFi cutout
* Perform speech recognition on edge - similar to Pocketsphinx.js
* Require users to login with own details
* Teacher (creator of room) admits students into room
* Mobile phone compatible
* Create our own speech-to-text model
* Allow users to correct transcription where necessary to improve the model