import os
import pyaudio
from vosk import Model, KaldiRecognizer
from settings import RU_MODEL
from settings import UA_MODEL


class SpeechToText:
    def __init__(self, language):
        if language == 'ru':
            model_path = RU_MODEL
        elif language == 'ua':
            model_path = UA_MODEL
        else:
            raise ValueError("Unsupported language: " + language)

        if not os.path.exists(model_path):
            print(f"Please download a model for {language} and unpack as 'model' in the current folder.")
            exit(1)
        self.model = Model(model_path)
        self.rec = KaldiRecognizer(self.model, 16000)  # assumes 16kHz microphone

    def listen(self):
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
        stream.start_stream()
        print('Listening...')


        while True:
            data = stream.read(4000, exception_on_overflow=False)
            if len(data) == 0:
                break
            if self.rec.AcceptWaveform(data):
                result = self.rec.Result()
                print(result)
                return result.lower()
        print("Sorry, I didn't understand that.")
        return ""
