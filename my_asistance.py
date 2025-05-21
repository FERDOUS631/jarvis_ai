import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import webbrowser
import time
# Voice recognizer and text-to-speech setup
recognizer = sr.Recognizer()
jarvis = pyttsx3.init()
voices = jarvis.getProperty('voices')
jarvis.setProperty('voice', voices[1].id) 


def speak(text):
    print("Jarvis:", text)
    jarvis.say(text)
    jarvis.runAndWait()

def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print("🎙️ Listening...")
            recognizer.adjust_for_ambient_noise(source)
            voice = recognizer.listen(source)
            command = recognizer.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '').strip()
    except Exception as e:
        print("❌ Sorry sir, I didn't catch that. Could you please repeat?", e)
        speak("Sorry sir, I didn't catch that. Could you please repeat?")
    return command


def run_jarvis():
    command = take_command()

    if not command:
        return

    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The time is {time}")

    elif 'play' in command:
        song = command.replace('play', '').strip()
        speak(f"Yes sir, Playing {song}")
        pywhatkit.playonyt(song)

    elif 'portfolio' in command:
        speak("yes sir, Opening your portfolio")
        webbrowser.open("https://ferdousprotfolio.netlify.app/")

    elif 'facebook' in command:
        speak("yes sir, Opening Facebook profile")
        webbrowser.open("https://www.facebook.com/ferdous.reza.568")
    elif 'whatsapp' in command:
        speak("yes sir ,Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com/")

    elif 'github' in command:
        speak(" yes sir, Opening GitHub profile")
        webbrowser.open("https://github.com/FERDOUS631")

    elif 'open google' in command:
        speak("yes sir, Opening Google")
        webbrowser.open("https://www.google.com")

    elif 'who is' in command or 'tell me' in command:
        try:
            info = wikipedia.summary(command, sentences=2)
            print(info)
            speak(info)
        except:
            speak("Sorry sir, I couldn't find anything on that topic.")
    elif 'exit' in command or 'quit' in command or 'stop' in command:
        speak("okk.Goodbye sir!")
        exit()
    else:
        speak("okk sir ,i'm searching for you")
        pywhatkit.search(command)
speak("Hi I am jarvis.How can I assist you today?")
# Main loop
time.sleep(2)
speak("I am ready to assist you")
while True:
    run_jarvis()
