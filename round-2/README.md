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

### Next Steps:

* Speech-to-text AI on edge
* When speech is detected -> text is sent live to all other devices connected to private room
* The AI will detect the internet bandwidth
* The text will appear only if somebody has low bandwidth
* If somebody's internet connection is lost completely and (s)he is reconnected again, the AI will show the person what (s)he has missed in the last few minutes through text
