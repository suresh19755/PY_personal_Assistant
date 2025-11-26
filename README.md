# PY_personal_Assistant
A Python-based virtual assistant featuring a modern dark-mode Tkinter GUI. Capable of voice-controlled web automation (YouTube, Google), system management (screenshots, locking), and interactive data visualization.

🎙️ Python AI Desktop Voice Assistant with GUI
A Python-based virtual desktop assistant featuring a modern dark-mode GUI built with Tkinter. This assistant automates daily tasks, performs web searches, controls system functions, and visualizes data using voice commands.

📋 Table of Contents :
Overview

Key Features

User Interface

Installation & Setup

Usage

Dependencies

🧐 Overview :
This project integrates Speech Recognition and Text-to-Speech (TTS) engines to create an interactive assistant. Unlike simple command-line scripts, this assistant features a responsive Graphical User Interface (GUI) that displays real-time logs of the conversation, command suggestions, and visual status indicators.

The application remembers the user's name across sessions using local file storage (user_data.txt) and handles tasks using multi-threading to ensure the GUI remains responsive while listening or speaking.

✨ Key Features :
🌐 Web & Knowledge
YouTube Playback: "Play [Song Name]" plays video directly on YouTube.

Wikipedia Search: "Wikipedia [Topic]" reads a 2-sentence summary.

Google Search: "Search [Query]" opens a browser search.

⚙️ System Automation (Windows) :
App Launching: Opens Notepad and Calculator.

Screen Capture: "Take Screenshot" saves the current screen with a timestamp.

System Security: "Lock System" immediately locks the workstation.

📊 Productivity & Tools :
Data Visualization: "Show Chart" generates a sample Matplotlib bar chart.

Time & Date: verbalizes the current time and date.

Personalization: Remembers and greets the user by name.

🎉 Entertainment :
Jokes: Tells random programming jokes using pyjokes.

🎨 User Interface :
The GUI is designed with a modern "Dark Mode" aesthetic:

Color Scheme: Dark Grey Background (#2b2b2b) with Teal Accents (#00cec9).

Components: * Live Status Label (Listening/Processing/Ready).

Scrollable Console Log (Displays User vs. System dialogue).

"Tap to Speak" button for manual activation.

🛠️ Installation & Setup :
1. Clone the Repository
Bash

git clone https://github.com/yourusername/voice-assistant.git
cd voice-assistant
2. Install Dependencies
This project relies on several external libraries. You can install them using pip:

Bash

pip install tk speechrecognition pyttsx3 pywhatkit wikipedia pyjokes pyautogui matplotlib
> Note: You may also need to install pyaudio for microphone access. If pip install pyaudio fails, try downloading the specific .whl file for your python version or use pip install pipwin followed by pipwin install pyaudio.

3. Run the Application
Bash

python personal_assistant.py
🗣️ Usage
Run the script to open the GUI.

Wait for the "System Ready" status.

Click the "TAP TO SPEAK" button.

Speak a command (e.g., "Play Blinding Lights" or "Open Calculator").

Check the console log to see how the assistant interpreted your voice.

📦 Dependencies :
tkinter: Standard Python GUI library.

speech_recognition: Google Speech API integration.

pyttsx3: Offline Text-to-Speech conversion.

pywhatkit: For YouTube automation.

matplotlib: For generating data charts.

pyautogui: For screenshots.

pyjokes: For fetching jokes.

📝 Code Structure :
AssistantGUI: Main class handling the window and UI elements.

process_command(): The logic core that parses voice strings and triggers actions.

threading: Used to run the listening loop separately from the GUI main loop to prevent freezing.

*Demo :
<img width="595" height="838" alt="Screenshot 2025-11-26 183028" src="https://github.com/user-attachments/assets/67f54b2d-1a44-4298-9477-e1f50678a2b8" />

Made by [Suresh seervi]

Disclaimer: System commands like lock system and notepad are optimized for the Windows Operating System. Linux/Mac users may need to adjust the os.system calls.
