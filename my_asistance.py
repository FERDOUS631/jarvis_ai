import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import webbrowser

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
        print("❌ Could not understand. Error:", e)
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
        speak("Opening your portfolio")
        webbrowser.open("https://ferdousprotfolio.netlify.app/")

    elif 'facebook' in command:
        speak("Opening Facebook profile")
        webbrowser.open("https://www.facebook.com/ferdous.reza.568")

    elif 'github' in command:
        speak("Opening GitHub profile")
        webbrowser.open("https://github.com/FERDOUS631")

    elif 'open google' in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif 'who is' in command or 'tell me' in command:
        try:
            info = wikipedia.summary(command, sentences=2)
            print(info)
            speak(info)
        except:
            speak("Sorry, I couldn't find anything on that topic.")
    elif 'exit' in command or 'quit' in command or 'stop' in command:
        speak("okk.Goodbye sir!")
        exit()
    else:
        speak("Searching that for you")
        pywhatkit.search(command)
speak("Hi I am jarvis.How can I assist you today?")
# Main loop
while True:
    run_jarvis()
