import os
import pyaudio
from vosk import Model, KaldiRecognizer
from settings import RU_MODEL
from settings import RU_MODEL_SMALL
from settings import UA_MODEL


class SpeechToText:
    def __init__(self, language):
        if language == 'ru':
            model_path = RU_MODEL_SMALL
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

        # # List all audio input devices
        # for i in range(p.get_device_count()):
        #     device_info = p.get_device_info_by_index(i)
        #     if device_info['maxInputChannels'] > 0:
        #         print(f"Device id {i} - {device_info['name']}")



        while True:
            data = stream.read(4000, exception_on_overflow=False)
            if len(data) == 0:
                break
            if self.rec.AcceptWaveform(data):
                result = self.rec.Result()
                print(result)
                return result.lower()
            else:
                result = self.rec.PartialResult()
                #print(self.rec.PartialResult())
                #return result.lower()
        print("Sorry, I didn't understand that.")
        return ""
