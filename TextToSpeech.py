import pyttsx3


class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('language', 'ru')


    def speak(self, text):
        self.engine.setProperty('language', 'ru')

        self.engine.say(text)
        self.engine.runAndWait()
