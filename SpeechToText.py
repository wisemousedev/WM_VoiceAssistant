import speech_recognition as sr
import pyttsx3


class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source, phrase_time_limit=5)
            try:
                text = self.recognizer.recognize_google(audio)
                #text = self.recognizer.recognize_google(audio, language='ru-RU')
                print(text)
                return text.lower()
            except:
                print("Sorry, I didn't understand that.")
                return ""

