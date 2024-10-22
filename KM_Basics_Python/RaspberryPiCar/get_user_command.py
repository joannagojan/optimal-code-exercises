import speech_recognition as sr


def get_car_command() -> str:
    r = sr.Recognizer()
    with sr.Microphone as source:

        # getting a single command using listen()
        audio = r.listen(source)
        try:
            print('Waiting for a command...')
            command = r.recognize_google(audio, language='en-au')
            print('voice text: ' + command)
        except Exception as e:
            print(e)
            return 'error'
    return command


def main() -> None:
    command = get_car_command()


if __name__ == '__main__':
    main()
