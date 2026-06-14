import speech_recognition as sr
import pyttsx3
import datetime

# voice engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        command = command.lower()
        print("You said:", command)
    except:
        speak("Sorry, I could not understand")
        return ""

    return command


def show_time():
    time_now = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The time is " + time_now)


def assistant():
    speak("Hello, I am your assistant")

    while True:
        command = take_command()

        if command == "":
            continue

        # TIME
        if "time" in command:
            show_time()

        # EXIT
        elif "exit" in command or "stop" in command:
            speak("Goodbye")
            break

        else:
            speak("I did not understand that")


if __name__ == "__main__":
    assistant()