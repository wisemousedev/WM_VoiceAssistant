import pyttsx3


class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\TokenEnums\RHVoice\Irina')
        self.engine.setProperty('rate', 130)
        # from https://rhvoice.org/download/RHVoice-voice-Russian-Irina-v4.1.2012.18-setup.exe


    def speak(self, text):

        self.engine.say(" " + text)
        self.engine.runAndWait()

