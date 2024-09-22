# 1. Losuj dwie liczby z przedziału [100, 300] do zmiennych a i b, dopóki liczba a nie będzie mniejsza
# od liczby b o minimum 10. Następnie sprawdź, ile liczb w przedziale [a, b] jest podzielnych przez
# wartość pod zmienną x, którą pobierzesz od użytkownika.

import random

def two_one() -> list:

    result_list = []

    def get_random() -> int:
        return random.randint(100, 300)

    def get_difference(a: int, b: int) -> float:
        return abs(a - b)

    while True:
        a, b = get_random(), get_random()

        if get_difference(a, b) > 10:
            user_int = int(input("Input an integer: \n"))

            for integer in range(min(a,b), max(a,b)):
                if integer % user_int == 0:
                    result_list.append(integer)
            break



    return result_list


for number in two_one():
    print(number)

