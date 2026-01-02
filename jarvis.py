import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How can I help you today?")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except:
        speak("Sorry, I did not understand.")
        return ""

def process_command(command):
    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")

    elif "date" in command:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {date}")

    elif "wikipedia" in command:
        speak("Searching Wikipedia")
        command = command.replace("wikipedia", "")
        result = wikipedia.summary(command, sentences=2)
        speak(result)

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")

    elif "your name" in command:
        speak("My name is Jarvis, your personal AI assistant")

    elif "exit" in command or "quit" in command:
        speak("Goodbye! Have a great day")
        exit()

    else:
        speak("Sorry, I cannot do that yet")

# Main Program
wish_user()
while True:
    cmd = take_command()
    if cmd != "":
        process_command(cmd)
