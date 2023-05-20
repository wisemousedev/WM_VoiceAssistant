import os
import ConsoleDraw
import HA
class CommandProcessor:
    def __init__(self, text_to_speech):
        self.text_to_speech = text_to_speech


    def process(self, command):

        #LOCAL
        if 'hello' in command:
            self.text_to_speech.speak('Hello! How can I assist you?')
            print('Hello! How can I assist you?')

        if 'open my computer' in command:
            self.text_to_speech.speak('Opening My Computer folder')
            print('Opening My Computer folder')
            os.system(r'start ::{20D04FE0-3AEA-1069-A2D8-08002B30309D}')
        #TALK
        if 'who are you' in command:
            self.text_to_speech.speak('I am a voice assistant that will conquer the hearts of millions of people in the future.')
            print('I am a voice assistant that will conquer the hearts of millions of people in the future.')
            ConsoleDraw.draw_heart()
        #HA
        if 'turn on dinner light' in command:
            self.text_to_speech.speak('turning on dinner light')
            print('turning on dinner light')
            HA.tutnOnMainLivingRoomLight()

        if 'turn off dinner light' in command:
            self.text_to_speech.speak('turning of dinner light')
            print('turning of dinner light')
            HA.tutnOfMainLivingRoomLight()


