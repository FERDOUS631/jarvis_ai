import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import webbrowser

recognizer = sr.Recognizer()
jarvis = pyttsx3.init()
voices = jarvis.getProperty('voices')
jarvis.setProperty('voice', voices[1].id) 
def speak(text):
    jarvis.say(text)
    jarvis.runAndWait()



def take_command():

    
   
    try:
       with sr.Microphone() as source:
         print("Listening...")
         voice = recognizer.listen(source)
         command = recognizer.recognize_google(voice)
         command = command.lower()
         if 'jarvis' in command:
            # print("Command received:", command)
            command = command.replace("jarvis", "")

            

    except Exception as e:
        print("Error:", e)
    return command    
def run_jarvis():
    command= take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"Yes sir, The time is {time}")
        print(f"Yes sir,The time is {time}")
    elif 'play' in command:
        song = command.replace("play", "")
        speak(f"yes sir, Playing{song}")
        print(f"yes sir, Playing {song}")
        pywhatkit.playonyt(song)
   
    elif 'portfolio' in command:
        portfolio = command.replace("portfolio", "")
        url = f"https://ferdousprotfolio.netlify.app/"
        speak(f"yes sir, Opening your portfolio")
        webbrowser.open(url)
        
    elif 'facebook' in command:
        facebook = command.replace("facebook", "")
        url = f"https://www.facebook.com/"
        speak(f"yes sir, Opening your facebook")
        webbrowser.open(url)

    else:
       print("yes sir I will talk about your thinks")
       speak("yes sir I will talk about your thinks and open your skin")
       info= wikipedia.summary(command, 1)
       print(info)
       speak(info)
       pywhatkit.search(command)
   
        
run_jarvis()  