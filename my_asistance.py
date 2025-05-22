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
# jarvis.setProperty('voice', voices[1].id) 

selected_voice = voices[1]  
jarvis.setProperty('voice', selected_voice.id)

# Gender-based title
if "female" in selected_voice.name.lower():
    user_title = "ma'am"
else:
    user_title = "sir"

love_question_count = 0
def speak(text):
    print("Jarvis:", text)
    jarvis.say(text)
    jarvis.runAndWait()

def greet_user():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        speak("Good morning !")
    elif 12 <= hour < 17:
        speak("Good afternoon !")
    elif 17 <= hour < 22:
        speak("Good evening !")
    else:
        speak("Good night!")
def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print("🎙️ Listening...")
            speak("I am ready listening to start your command.Now, how can I help you today? 🎙️")
            recognizer.adjust_for_ambient_noise(source)
            voice = recognizer.listen(source)
            command = recognizer.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '').strip()
    except Exception as e:
        print("❌ Sorry sir, I didn't catch that. Could you please repeat?", e)
        # speak("Sorry sir, I didn't catch that. Could you please repeat?")
    return command


def run_jarvis():
    command = take_command()

    if not command:
        return

    if 'time ' in command:
        time_now = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"{user_title} The time is {time_now}")

    elif 'date' in command or 'day' in command:
        date = datetime.datetime.now().strftime('%A, %B %d, %Y')
        speak(f"{user_title} The date is {date}")


    elif 'you' in command or 'love' in command or 'me' in command:
        global love_question_count

        love_question_count += 1
        if love_question_count == 1:
            speak(f"Yes {user_title}, I love you. You are my creator and I am here to assist you.")
        elif love_question_count == 2:
            speak(f"Haha {user_title}, you've already asked that. My love remains the same!")
        elif love_question_count == 3:
            speak(f"Of course {user_title}, I love you. But let's not make it a habit to ask too often.")
        elif love_question_count == 4:
            speak(f"Yes {user_title}, I love you. But remember, I am just a program.")
        elif love_question_count == 5:
           speak("I love you too but I am  As your AI assistant, I dont have feelings like humans do. But I am here to assist you with anything you need")
        elif love_question_count == 6:
            speak(" I'm here to help you with full attention and support — you could say that's a kind of love!But not the human kind  — I'm your loyal assistant, always ready when you need me.")
        else:
            speak(f"{user_title}, I always love you, no matter how many times you ask.")
   

      

    elif 'who are you' in command or 'what are you' in command:
        speak(f"yes {user_title}, I am Jarvis, your personal assistant. I am here to help you with your tasks and provide information.")

    elif 'play' in command:
        song = command.replace('play', '').strip()
        speak(f"Yes {user_title}, Playing {song}")
        pywhatkit.playonyt(song)


    elif 'portfolio' in command and 'developer' in command:
        speak(f"yes {user_title}, Opening your portfolio")
        webbrowser.open("https://ferdousprotfolio.netlify.app/")


    elif 'facebook' in command:
        speak(f"yes {user_title}, Opening Facebook profile")
        webbrowser.open("https://www.facebook.com")

    elif 'instagram' in command:
        speak(f"yes {user_title}, Opening Instagram profile")
        webbrowser.open("https://www.instagram.com")

    elif 'linkedin' in command:
        speak(f"yes {user_title}, Opening LinkedIn profile")
        webbrowser.open("https://www.linkedin.com")

    elif 'twitter' in command:
        speak(f"yes {user_title}, Opening Twitter profile")
        webbrowser.open("https://twitter.com")

    elif 'whatsapp' in command:
        speak(f"yes {user_title} ,Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com/")

    elif 'github' in command:
        speak(f"yes {user_title}, Opening GitHub profile")
        webbrowser.open("https://github.com")

    elif 'open google' in command:
        speak(f"yes {user_title}, Opening Google")
        webbrowser.open("https://www.google.com")

    elif  'know' in command and 'about' in command:
       try:
           know = command.replace('know', '').replace('about', '').strip()
           speak(f'yes {user_title}  , I {know}')
           into = wikipedia.summary(command, sentences=1)
           print(into)  
           speak(into)
           pywhatkit.search(know)
          
       except:
           speak(f"Sorry {user_title}, I couldn't  anything on that topic.")
    elif 'who is' in command or 'tell me' in command :
        try:
            tell = command.replace('who is', '').replace('tell me', '').strip()
            speak(f"yes {user_title}, I am searching for you to {tell} ")
            info = wikipedia.summary(command, sentences=1)
            print(info)
            speak(info)
            pywhatkit.search(tell)
        except:
            speak("Sorry sir, I couldn't find anything on that topic. to try search on google")
            pywhatkit.search(command)
    elif 'exit' in command or 'quit' in command or 'stop' in command:
        speak(f"ok .Goodbye {user_title}! I am shutting down now.")
        time.sleep(2)
        speak("Thank you for using me. Have a great day!")
        
        exit()
    else:
        speak(f"ok {user_title} ,i'm searching for you")
        pywhatkit.search(command)

# Greet the user
greet_user()
speak("Hi I am jarvis. How can I assist you today?")
# Main loop
time.sleep(2)
speak("I am ready to assist you")
while True:
    run_jarvis()
