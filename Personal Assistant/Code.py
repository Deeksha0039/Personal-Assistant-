import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening! I am your assistant. How can I help you?")
        


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query)
    except sr.UnknownValueError:
        speak("Sorry, I did not catch that. Please say that again.")
        return ""
    except sr.RequestError:
        speak("Sorry, I am unable to connect to the recognition service.")
        return ""
    except Exception as e:
        speak(f"An error occurred: {str(e)}")
        return ""
    return query.lower()

if __name__ == "__main__":
    wish()
    while True:
        query = takeCommand()
        if not query:
            continue
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            try:
                result = wikipedia.summary(query.replace("wikipedia", ""), sentences=2)
                speak("According to Wikipedia")
                speak(result)
            except Exception:
                speak("Sorry, I couldn't find any results on Wikipedia.")
        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")
        elif 'open google' in query:
            webbrowser.open("https://google.com")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'exit' in query or 'quit' in query or 'stop' in query:
            speak("Goodbye!")
            break
