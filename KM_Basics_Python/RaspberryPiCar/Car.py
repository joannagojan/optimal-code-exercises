class Car:
    def __init__(self):
        self.speed = 0  # in percentage
        self.direction = 'stop'

        # TODO validation

    # ----------- SPEED --------------

    def set_speed(self, speed: int) -> None:
        self.speed = speed

    def get_speed(self) -> int:
        return self.speed

    def slow_down(self) -> None:
        self.speed = max(0, self.speed - 25)

    def go_faster(self) -> None:
        self.speed = min(100, self.speed + 25)

    def stop_car(self) -> None:
        self.direction = 'forward'
        self.speed = 0

    # ----------- DIRECTION --------------

    def set_direction(self, direction: str) -> None:
        self.direction = direction

    def get_direction(self) -> str:
        return self.direction

    def go_left(self) -> None:
        self.direction = 'left'

    def go_right(self) -> None:
        self.direction = 'right'

    def go_forward(self) -> None:
        self.direction = 'forward'

    # ----------- MOVEMENTS ------------

    def start_car(self) -> None:
        self.direction = 'forward'
        self.speed = 25
