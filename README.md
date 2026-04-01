# KeyloggerGUI

##📌 Overview
A Keylogger is a Python-based project that records keyboard inputs using a graphical interface built with Tkinter. A keylogger is a tool that captures every keystroke typed by a user. The project stores data in text and JSON files and is used for educational purposes to understand keylogging and cybersecurity risks.

# ⚙️ Features
Simple and user-friendly GUI using Tkinter
Captures keyboard inputs in real-time
Stores logs in both .txt and .json formats
Start and Stop keylogging functionality
Lightweight and easy to use

# 🛠️ Technologies Used
. Python
. Tkinter (GUI)
. pynput (keyboard listener)
. JSON (structured data storage)
. File Handling

# 🚀 How It Works
The application listens to keyboard events using the pynput library.
Whenever a key is pressed, it is recorded and saved into files.
The GUI allows users to control the logging process easily.

### Install required libraries
```bash
pip install pynput
```

### Run the program
```bash
python keylogger.py
```
# 📂 Output Files
logs.txt → Stores keystrokes in plain text
logs.json → Stores keystrokes in structured format

# ⚠️ Disclaimer
This project is created only for educational purposes to understand how keyloggers work and how to defend against them.
Do not use this tool for unauthorized monitoring or malicious activities.

# 📸 Future Improvements
Encryption of logged data
Email reporting system
Advanced UI design
