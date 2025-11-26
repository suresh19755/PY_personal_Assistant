import tkinter as tk
from tkinter import messagebox
import threading
import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser
import os
import matplotlib.pyplot as plt
import datetime
import wikipedia
import pyjokes
import pyautogui
import ctypes

# --- Color Palette ---
COLOR_BG = "#2b2b2b"        # Dark Grey Background
COLOR_ACCENT = "#00cec9"    # Modern Teal
COLOR_TEXT = "#dfe6e9"      # Off-white text
COLOR_BTN_HOVER = "#81ecec" # Lighter Teal
COLOR_ERROR = "#ff7675"     # Soft Red
COLOR_CONSOLE = "#1e1e1e"   # Very Dark Grey for console

USER_DATA_FILE = "user_data.txt"

class AssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Assistant")
        self.root.geometry("550x780")
        self.root.configure(bg=COLOR_BG)

        self.username = self.load_name()

        # Initialize Engines
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 170) 
        self.listener = sr.Recognizer()

        # --- Header Section ---
        header_frame = tk.Frame(root, bg=COLOR_BG)
        header_frame.pack(pady=30)
        
        self.status_label = tk.Label(header_frame, text="System Ready", 
                                     font=("Segoe UI", 24, "bold"), 
                                     bg=COLOR_BG, fg=COLOR_ACCENT)
        self.status_label.pack()

        sub_label = tk.Label(header_frame, text="Waiting for input...", 
                             font=("Segoe UI", 10), 
                             bg=COLOR_BG, fg="grey")
        sub_label.pack(pady=5)

        # --- Command List (Styled Card) ---
        cmd_frame = tk.Frame(root, bg="#353b48", bd=0) 
        cmd_frame.pack(pady=20, padx=40, fill="x", ipady=15)

        tk.Label(cmd_frame, text="AVAILABLE COMMANDS", 
                 font=("Segoe UI", 9, "bold"), 
                 bg="#353b48", fg="#b2bec3").pack(pady=(10, 5), anchor="w", padx=20)

        commands_text = (
            "• Play [Song Name]\n"
            "• Wikipedia [Topic]\n"
            "• Google Search [Query]\n"
            "• Take Screenshot\n"
            "• Tell me a joke\n"
            "• Remember my name is [Name]\n"
            "• Open Notepad / Calculator\n"
            "• Lock System"
        )
        
        tk.Label(cmd_frame, text=commands_text, 
                 font=("Segoe UI", 11), 
                 bg="#353b48", fg=COLOR_TEXT, justify="left").pack(anchor="w", padx=20)

        # --- Action Buttons ---
        btn_frame = tk.Frame(root, bg=COLOR_BG)
        btn_frame.pack(pady=30)

        self.speak_btn = tk.Button(btn_frame, text="TAP TO SPEAK", 
                                   font=("Segoe UI", 12, "bold"), 
                                   bg=COLOR_ACCENT, fg="#2d3436", 
                                   activebackground=COLOR_BTN_HOVER,
                                   relief="flat", bd=0, 
                                   width=20, height=2,
                                   command=self.start_listening_thread)
        self.speak_btn.pack(pady=10)

        self.stop_btn = tk.Button(btn_frame, text="EXIT SYSTEM", 
                                  font=("Segoe UI", 10, "bold"), 
                                  bg=COLOR_BG, fg=COLOR_ERROR, 
                                  activebackground=COLOR_BG, activeforeground="white",
                                  relief="flat", bd=0, 
                                  command=self.stop_assistant)
        self.stop_btn.pack()

        # --- Terminal Output ---
        self.console_text = tk.Text(root, height=10, width=50, 
                                    font=("Consolas", 9), 
                                    bg=COLOR_CONSOLE, fg=COLOR_ACCENT,
                                    bd=0, highlightthickness=0)
        self.console_text.pack(pady=10, padx=20, fill="x")

        # Initial Greeting
        self.root.after(1000, self.wish_me)

    def load_name(self):
        """Checks if user_data.txt exists and reads the name."""
        if os.path.exists(USER_DATA_FILE):
            with open(USER_DATA_FILE, "r") as f:
                return f.read().strip()
        return "User"

    def save_name(self, name):
        """Saves the name to user_data.txt."""
        with open(USER_DATA_FILE, "w") as f:
            f.write(name)
        self.username = name

    def update_status(self, text, is_user=False):
        self.status_label.config(text=text)
        prefix = ">> USER: " if is_user else ">> SYSTEM: "
        self.console_text.insert(tk.END, prefix + text + "\n")
        self.console_text.see(tk.END)
        self.root.update()

    def speak(self, text):
        self.update_status(text)
        self.engine.say(text)
        self.engine.runAndWait()

    def wish_me(self):
        hour = int(datetime.datetime.now().hour)
        if 0 <= hour < 12:
            greeting = "Good Morning"
        elif 12 <= hour < 18:
            greeting = "Good Afternoon"
        else:
            greeting = "Good Evening"
        
        # Personalized Greeting
        threading.Thread(target=self.speak, args=(f"{greeting} {self.username}. System online.",)).start()

    def start_listening_thread(self):
        self.speak_btn.config(text="LISTENING...", bg="#ffeaa7") 
        thread = threading.Thread(target=self.process_command)
        thread.start()

    def process_command(self):
        command = self.take_command()

        if not command:
            self.reset_gui()
            return

        if 'play' in command:
            song = command.replace('play', '').strip()
            self.speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)

        elif 'wikipedia' in command:
            self.speak("Searching Wikipedia...")
            query = command.replace('wikipedia', '').strip()
            try:
                results = wikipedia.summary(query, sentences=2)
                self.speak("According to Wikipedia")
                self.speak(results)
            except:
                self.speak("I couldn't find any results for that.")

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            self.speak(f"Current time is {time}")

        elif 'date' in command:
            today = datetime.date.today().strftime("%B %d, %Y")
            self.speak(f"Today's date is {today}")

        elif 'search' in command: 
            query = command.replace('search', '').strip()
            self.speak(f"Searching web for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")

        elif 'remember my name is' in command:
            name = command.replace('remember my name is', '').strip()
            self.save_name(name)
            self.speak(f"Nice to meet you, {name}. I will remember that.")

        elif 'screenshot' in command:
            self.speak("Taking screenshot")
            self.root.iconify() 
            pyautogui.sleep(1) 
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"screenshot_{timestamp}.png"
            pyautogui.screenshot(filename)
            self.root.deiconify() 
            self.speak(f"Screenshot saved")

        elif 'joke' in command:
            joke = pyjokes.get_joke()
            self.speak(joke)

        elif 'lock' in command and 'system' in command:
            self.speak("Locking the system")
            ctypes.windll.user32.LockWorkStation()

        elif 'chart' in command or 'graph' in command:
            self.generate_chart()

        elif 'notepad' in command:
            self.speak("Launching Notepad")
            os.system('notepad') 

        elif 'calculator' in command:
            self.speak("Launching Calculator")
            os.system('calc')

        elif 'stop' in command or 'exit' in command:
            self.speak("Shutting down")
            self.stop_assistant()
            return

        else:
            self.speak("Command not recognized.")
        
        self.reset_gui()

    def take_command(self):
        command = ""
        try:
            with sr.Microphone() as source:
                self.status_label.config(text="Listening...")
                self.listener.adjust_for_ambient_noise(source) 
                voice = self.listener.listen(source)
                
                self.status_label.config(text="Processing...")
                command = self.listener.recognize_google(voice)
                command = command.lower()
                self.update_status(command, is_user=True)
                
        except sr.UnknownValueError:
            self.speak("Audio not clear.")
        except sr.RequestError:
            self.speak("Network Error.")
        except Exception as e:
            print(f"Error: {e}")
        
        return command

    def generate_chart(self):
        self.speak("Visualizing data.")
        plt.style.use('dark_background')
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
        sales = [1500, 2300, 1800, 3200, 2900]
        fig, ax = plt.subplots(figsize=(8, 5))
        bars = ax.bar(months, sales, color=COLOR_ACCENT)
        ax.set_title('Monthly Sales Performance', color='white', pad=20)
        ax.set_ylabel('Sales ($)', color='white')
        ax.grid(axis='y', linestyle='--', alpha=0.3, color='gray')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.show()

    def reset_gui(self):
        self.speak_btn.config(text="TAP TO SPEAK", bg=COLOR_ACCENT)
        self.status_label.config(text="System Ready")

    def stop_assistant(self):
        self.root.destroy()
        os._exit(0)

if __name__ == "__main__":
    root = tk.Tk()
    app = AssistantGUI(root)
    root.mainloop()