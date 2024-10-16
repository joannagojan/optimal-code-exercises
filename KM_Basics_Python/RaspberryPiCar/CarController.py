from RaspberryPiCar.Car import Car


class CarController:
    def __init__(self, car: Car):
        self.car = car
        self.all_commands = {
            'straight': {'straight', 'forward', 'ahead'},
            'left': {'left'},
            'right': {'right'},
            'move': {'start', 'move', 'go'},
            'fast': {'faster', 'fast'},
            'slow': {'slow', 'slower',},
            'stop': {'stop'}
        }

    def receive_command(self, user_command: str):

        user_commands = set(user_command.split())

        if user_commands & self.all_commands.get('stop'):
            print('Stopping')
            self.car.stop_car()
        else:
            # ----------- DIRECTION --------------

            if user_commands & self.all_commands.get('straight'):
                print('Going forward')
                self.car.go_forward()
            elif user_commands & self.all_commands.get('left'):
                print('Turning left')
                self.car.go_left()
            elif user_commands & self.all_commands.get('right'):
                print('Turning right')
                self.car.go_right()

            # ----------- SPEED --------------

            if user_commands & self.all_commands.get('move'):
                print('Starting the car')
                self.car.start_car()
            elif user_commands & self.all_commands.get('fast'):
                print('Going faster')
                self.car.go_faster()
            elif user_commands & self.all_commands.get('slow'):
                print('Going slower')
                self.car.go_faster()



        if user_command == 'error':
            print('Could not get a command, default option instead...')
            self.car.start_car()


c1 = Car()

cc1 = CarController(c1)

cc1.receive_command('left hihi haha faster right')
