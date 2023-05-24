import os
import ConsoleDraw
import HA
import tempfile


class CommandProcessorRU:

    def __init__(self, text_to_speech):
        self.text_to_speech = text_to_speech

    def process(self, command):

        #LOCAL
        if 'привет' in command:
            self.text_to_speech.speak('Привет! Как Я могу помочь??')
            print('Привет! Как Я могу помочь?')

        if 'открой мой компьютер' in command:
            self.text_to_speech.speak('Opening My Computer folder')
            print('Opening My Computer folder')
            os.system(r'start ::{20D04FE0-3AEA-1069-A2D8-08002B30309D}')
        #TALK
        if 'кто ты' in command:
            self.text_to_speech.speak('Я - голосовой помощник, который в будущем покорит сердца миллионов людей.')
            print('Я - голосовой помощник, который в будущем покорит сердца миллионов людей.')
            ConsoleDraw.draw_heart()
        #HA
        if 'включи люстру' in command:
            self.text_to_speech.speak('включаю люстру')
            print('turning on dinner light')
            HA.turnOnMainLivingRoomLight()

        if 'выключи люстру' in command:
            self.text_to_speech.speak('выключаю люстру')
            print('turning of dinner light')
            HA.turnOfMainLivingRoomLight()

        if 'включи подсветку телевизора' in command:
            self.text_to_speech.speak('включаю подсветку телевизора')
            print('включаю подсветку телевизора')
            HA.turnTVLight()




