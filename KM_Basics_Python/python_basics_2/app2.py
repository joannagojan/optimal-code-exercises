
# 2. Pobieraj od użytkownika dwie liczby do zmiennych a i b, dopoki ich suma nie będzie liczbą parzystą.
# Następnie sprawdź, czy liczba a dzieli się przez liczbę lub na odwrót.


def three_two() -> str:

    result_str = ""

    def get_user_int(name: str) -> int:
        return int(input(f"Input an integer {name}: \n"))

    def is_divisible(x: int, y: int):
        if y != 0:
            if x % y == 0:
                return f'{x} is divisible by {y}'
            else:
                return f'{x} is NOT divisible by {y}'
        else:
            return "Cannot divide by 0"

    while True:
        a, b = get_user_int("a"), get_user_int("b")

        if (a + b) % 2 == 0:
            result_str += is_divisible(a, b) + "\n"
            if a != b :
                result_str +=is_divisible(b, a)
            break

        print("Try again")


    return result_str

print(three_two())




