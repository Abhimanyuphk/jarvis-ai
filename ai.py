import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import pyautogui
import wikipedia
import pywhatkit
import random
import psutil
import requests

# ---------------- VOICE ENGINE ----------------

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# ---------------- GREETING ----------------

def greet():
    hour = int(datetime.datetime.now().hour)

    if hour < 12:
        speak("Good morning Abhimanyu")
    elif hour < 17:
        speak("Good afternoon Abhimanyu")
    else:
        speak("Good evening Abhimanyu")

    speak("Jarvis system activated")

# ---------------- LISTEN ----------------

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You:", command)
        return command.lower()
    except:
        return ""

# ---------------- WEATHER ----------------

def weather():
    city = "Delhi"
    try:
        url = f"https://wttr.in/{city}?format=3"
        data = requests.get(url).text
        speak(data)
    except:
        speak("Weather information not available")

# ---------------- SYSTEM STATUS ----------------

def system_status():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent

    speak(f"CPU usage is {cpu} percent")
    speak(f"RAM usage is {ram} percent")

# ---------------- SCREENSHOT ----------------

def screenshot():
    img = pyautogui.screenshot()
    img.save("jarvis_screen.png")
    speak("Screenshot captured")

# ---------------- POWER FUNCTIONS ----------------

def shutdown():
    speak("Shutting down system")
    os.system("shutdown /s /t 5")

def restart():
    speak("Restarting computer")
    os.system("shutdown /r /t 5")

def lock():
    speak("Locking computer")
    os.system("rundll32.exe user32.dll,LockWorkStation")

# ---------------- OPEN APPS ----------------

def open_apps(query):
    if "chrome" in query:
        speak("Opening chrome")
        os.system("start chrome")

    elif "notepad" in query:
        speak("Opening notepad")
        os.system("notepad")

    elif "calculator" in query:
        speak("Opening calculator")
        os.system("calc")

# ---------------- JOKES ----------------

jokes = [
    "Why do programmers hate nature? Too many bugs.",
    "I told my computer I needed a break, and it froze.",
    "Why do Java developers wear glasses? Because they don't see sharp."
]

# ---------------- MAIN ----------------

greet()

while True:
    query = listen()

    if query == "":
        continue

    # EXIT
    if "exit" in query or "stop" in query:
        speak("Goodbye Abhimanyu")
        break

    # GOOGLE
    elif "open google" in query:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    # YOUTUBE
    elif "open youtube" in query:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    # SEARCH
    elif "search" in query:
        search = query.replace("search", "")
        speak("Searching " + search)
        webbrowser.open(f"https://google.com/search?q={search}")

    # MUSIC
    elif "play" in query:
        song = query.replace("play", "")
        speak("Playing " + song)
        pywhatkit.playonyt(song)

    # TIME
    elif "time" in query:
        time = datetime.datetime.now().strftime("%H:%M")
        speak("Current time is " + time)

    # WIKIPEDIA
    elif "who is" in query:
        person = query.replace("who is", "")
        try:
            info = wikipedia.summary(person, 2)
            speak(info)
        except:
            speak("Sorry, I couldn't find information")

    # WEATHER
    elif "weather" in query:
        weather()

    # SCREENSHOT
    elif "screenshot" in query:
        screenshot()

    # SYSTEM STATUS
    elif "system status" in query:
        system_status()

    # POWER
    elif "shutdown computer" in query:
        shutdown()

    elif "restart computer" in query:
        restart()

    elif "lock computer" in query:
        lock()

    # OPEN APPS
    elif "open" in query:
        open_apps(query)

    # JOKE
    elif "joke" in query:
        speak(random.choice(jokes))

    # EXTRA SMART RESPONSES
    elif "how are you" in query:
        speak("I am perfectly fine Abhimanyu")

    elif "your name" in query:
        speak("I am Jarvis, your assistant")

    elif "who made you" in query:
        speak("I was created by Abhimanyu")

    elif "battery" in query:
        battery = psutil.sensors_battery()
        speak(f"Battery is at {battery.percent} percent")

    elif "ip address" in query:
        ip = requests.get('https://api.ipify.org').text
        speak(f"Your IP address is {ip}")

    elif "hello" in query or "hi" in query:
        speak("Hello Abhimanyu, how can I help you")

    elif "thank you" in query:
        speak("You're welcome")

    else:
        speak("Sorry, I didn't understand that")