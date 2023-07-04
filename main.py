import Сommands
from CommandProcessor import CommandProcessor
from CommandProcessorRU import CommandProcessorRU
from SpeechToText import SpeechToText
from TextToSpeech import TextToSpeech



def main():
    speech_to_text = SpeechToText('ru')
    text_to_speech = TextToSpeech()
    #command_processor = CommandProcessor(text_to_speech)
    command_processor = CommandProcessorRU(text_to_speech)

    while True:
        command = speech_to_text.listen()
        if any(code in command for code in Сommands.WakeUP_Codes):
            text_to_speech.speak("Чем могу помочь?")
            while True:
                command = speech_to_text.listen_for_seconds(10)
                #command = speech_to_text.listen()
                if command:
                    command_processor.process(command)
                else:
                    break

if __name__ == "__main__":
    main()