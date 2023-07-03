import os
import ConsoleDraw
import HA
import ChatGPT
import HelperService
import LangChain
import Сommands
import re


class CommandProcessorRU:

    def __init__(self, text_to_speech):
        self.text_to_speech = text_to_speech

    def process(self, command):

            #HA
        if 'включи люстру' in command:
            self.text_to_speech.speak('включаю люстру')
            print('включаю люстру')
            HA.turnOnMainLivingRoomLight()

        if 'выключи люстру' in command:
            self.text_to_speech.speak('выключаю люстру')
            print('turning of dinner light')
            HA.turnOfMainLivingRoomLight()

        if 'включи подсветку телевизора' in command:
            self.text_to_speech.speak('включаю подсветку телевизора')
            print('включаю подсветку телевизора')
            HA.turnTVLight()

        if 'выключи подсветку телевизора' in command:
            self.text_to_speech.speak('выключаю подсветку телевизора')
            print('выключаю подсветку телевизора')
            HA.turnTVLightOff()

        if 'включи мой свет' in command:
            self.text_to_speech.speak('прам пам пам...')
            print('включаю свет')
            HA.turnFloodLightOn()

        if 'выключи мой свет' in command:
            self.text_to_speech.speak('прам пам пам...')
            print('выключаю свет')
            HA.turnFloodLightOff()

        if 'открой мой компьютер' in command:
            self.text_to_speech.speak('Открываю ваш компьютер')
            print('Opening My Computer folder')
            os.system(r'start ::{20D04FE0-3AEA-1069-A2D8-08002B30309D}')
        if any(code in command for code in Сommands.WakeUP_Codes):
            # ChatGPT
            #result = ChatGPT.runCompletion(command)
            result = LangChain.get_response_from_ai(command)
            self.text_to_speech.speak(result)
            print(result)




