from CommandProcessor import CommandProcessor
from SpeechToText import SpeechToText
from TextToSpeech import TextToSpeech


def main():
    speech_to_text = SpeechToText()
    text_to_speech = TextToSpeech()
    command_processor = CommandProcessor(text_to_speech)

    while True:
        command = speech_to_text.listen()
        command_processor.process(command)

if __name__ == "__main__":
    main()