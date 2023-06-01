import os
import ConsoleDraw
import HA
import ChatGPT
import HelperService
import Сommands


class CommandProcessorRU:

    def __init__(self, text_to_speech):
        self.text_to_speech = text_to_speech

    def process(self, command):

        #LOCAL
        if 'открой мой компьютер' in command:
            self.text_to_speech.speak('Открываю ваш компьютер')
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

        # if 'температура' in command:
        #     temperature = HelperService.stringToNumber(command)
        #     self.text_to_speech.speak(f'устанавливаю температуру в дома на {temperature} градуса')
        #     print(f'устанавливаю температуру в дома на {temperature} градусов')
        #     HA.turnFloodLightOff()

        #ChatGPT
        if any(code in command for code in Сommands.ChatGPT_CODES):
            self.text_to_speech.speak('Ищу инфу. Минутку...')
            result = ChatGPT.runCompletion(command)
            self.text_to_speech.speak(result)
            print(result)




