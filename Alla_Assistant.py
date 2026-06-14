import datetime
import os
import webbrowser
import speech_recognition as sr
import pyttsx3
import subprocess

print("Program Started")
assistant_name="Alla"
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def greet():
    print(f"Hello! i am {assistant_name}")
    speak(f"Hello! i am {assistant_name}")

def get_time():
    current_time=datetime.datetime.now()
    formatted_time=current_time.strftime("%H:%M:%S")
    return formatted_time

def get_date():
    current_date=datetime.datetime.now()
    formatted_date=current_date.strftime("%d-%m-%Y")
    return formatted_date

print("The current time is:",get_time())
print("The current date is:",get_date())
greet()
speak("Your voice assistant is ready")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand.")
        return ""
    except sr.RequestError:
        speak("Internet issue. Can't reach Google.")
        return ""

while True:
    command = take_command()

    if "hello" in command:
        speak("How are you?")

    elif "time" in command:
        speak("The current time is " + get_time())

    elif "date" in command:
        speak("Today's date is " + get_date())

    elif "open notepad" in command:
        speak("Opening Notepad")
        subprocess.Popen("notepad.exe")

    elif "search" in command:
        keyword = command.replace("search", "").strip()
        if keyword == "":
            speak("What should I search?")
        else:
            url = "https://www.google.com/search?q=" + keyword
            webbrowser.open(url)
            speak("Searching " + keyword)

    elif "stop" in command or "exit" in command:
        speak("Goodbye Laiba!")
        break

    else:
        if command != "":
            speak("Sorry, I don't understand this command.")
