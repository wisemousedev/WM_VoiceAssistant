import os
import openai
import speech_recognition as sr

from settings import OpenAI_API_KEY
openai.api_key = OpenAI_API_KEY

def whisper(audio):
    with open('speech.wav','wb') as f:
        f.write(audio.get_wav_data())
    speech = open('speech.wav', 'rb')
    wcompletion = openai.Audio.transcribe(
        model = "whisper-1",
        file=speech
    )
    user_input = wcompletion['text']
    #print(user_input)
    return user_input.lower()

