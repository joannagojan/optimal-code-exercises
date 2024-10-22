import socket
import concurrent.futures
import speech_recognition as sr
from typing import Callable


class CommandCar:
    def __init__(self):
        self.command = 'stop'


    def run_one_client_server(self) -> None:


        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostbyname(socket.gethostname())  # as not using a VB
        PORT = 9093

        server.bind((host, PORT))
        server.listen(1)

        # ------------------------------------
        def speech_recognize_command() -> None:
            r = sr.Recognizer()

            with sr.Microphone() as source:
                print("Give a car command...")
                r.adjust_for_ambient_noise(source)
                audio_text = r.listen(source)
                print("Time over, thanks")
                try:
                    message = r.recognize_google(audio_text, language='en-au')
                    print("Text: " + message)
                    return message
                except:
                    print("Sorry, I did not get that")


        def text_input_command() -> None:
            command = input("Give one word command...")
            if len(command.split()) > 1:
                raise ValueError("Command should be only one word")


        def get_command_in_real_time(command_input_fn: Callable):
            with concurrent.futures.ThreadPoolExecutor() as executor:
                while True:
                    future = executor.submit(command_input_fn)
                    return_value = future.result()
                    print(return_value)

        




        # ------- receive and send message methods-------
        def receive_message_from_socket(connection_socket: socket.socket) -> str:
            message = connection_socket.recv(1024).decode('utf-8')
            print(f'Message received: {message}')
            return message

        def send_message_to_socket(connection_socket: socket.socket, get_command_fn: Callable[[], str]) -> None:
            message = get_command_fn()
            connection_socket.send(message.encode('utf-8'))
            print(f'Message sent to client: {message}')


        while True:
            communication_socket, address = server.accept()
            get_command_in_real_time()

            receive_message_from_socket(communication_socket)

            send_message_to_socket(communication_socket, get_command_in_real_time)



        server.close()


def main() -> None:

    c = CommandCar()
    c.run_one_client_server()


if __name__ == "__main__":
    main()