import speech_recognition as sr
import pyttsx3
import STT_Whisper as wp


class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            self.recognizer.dynamic_energy_threshold = False
            self.recognizer.energy_threshold = 400
            audio = self.recognizer.listen(source, phrase_time_limit=10)
            try:
                #text = wp.whisper(audio)
                #text = self.recognizer.recognize_google(audio)
                text = self.recognizer.recognize_google(audio, language='ru-RU')
                print(text)
                return text.lower()
            except:
                print("Sorry, I didn't understand that.")
                return ""

