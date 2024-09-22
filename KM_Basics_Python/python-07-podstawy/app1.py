"""
1. Napisz program, w którym przewidziano menu, na podstawie którego użytkownik wybiera opcje:
"Liniowa", "Kwadratowa", "Sinus".

a. Kiedy użytkownik wybierze opcję "Liniowa", wtedy musi podać współczynniki a oraz b, żeby uzyskać
funkcję liniową postaci y = ax + b. Następnie podaje x i wyznacza wartość funkcji liniowej
dla tego x.

b. Kiedy użytkownik wybierze opcję "Kwadratowa", wtedy musi podać współczynniki a, b oraz c, żeby uzyskać
funkcję kwadratową postaci y = ax^2 + bx + c. Następnie podaje x i wyznacza wartość funkcji kwadratowej
dla tego x.

c. Kiedy użytkownik wybierze opcję "Sinus", wtedy podaje x i dla tego x wyznacza sinus.

Zadbaj o to, żeby w menu była opcja zakończenia programu, obsługa sytuacji, kiedy użytkownik poda zły
numer opcji oraz żeby po zrealizowaniu jednej operacji aplikacja pozwoliła na wykonywanie innych operacji.
"""
import math
from typing import Callable


def linear_formula(a: float, b: float) -> str:
    return f"{a}x + {b}"


def calculate_linear_function(a: float, b: float, x: float) -> float:
    return a * x + b


def quadratic_formula(a: float, b: float, c: float) -> str:
    return f"{a}x^2 + {b}*x + {c}"


def calculate_quadratic_formula(a: float, b: float, c: float, x: float) -> float:
    return a * x ** 2 + b * x + c


def do_operation(x: float, function: Callable):
    return function(x)


def calculate_sinus(x: float):
    return math.sin(x)


def get_input_until(condition: Callable[[float], bool], message: str) -> float | int:
    if not condition(x := float(input(f'Input number until {message}: \n'))):
        raise ValueError('Not a float')
        pass
    else:
        return x


def get_x_value():
    return float(get_input_until(lambda x: isinstance(x, float | int), "it's a float or an int"))


def menu() -> None:
    while True:
        try:
            print(" Choose function: 1. linear \n 2. quadratic \n 3. sinus \n 4. quit")
            function = int(get_input_until(lambda x: 1 <= x <= 4, "it's int between 1 and 4"))

            match function:
                case 1:
                    print('case 1')
                case 2:
                    a, b, c = float(get_input_until(lambda x: isinstance(x, float), "it's a float")), float(
                        get_input_until(lambda x: isinstance(x, float), "it's a float")), float(
                        get_input_until(lambda x: isinstance(x, float), "it's a float"))
                    print(quadratic_formula(a, b, c))
                    x = get_x_value()
                    print(x)
                    print(f'the result of the quadratic function {quadratic_formula(a, b, c)} and x: {x} is {calculate_quadratic_formula(x, a, b,c)}')
                case 3:
                    print("case 3")
                case 4:
                    print("case 4")
                case _:
                    continue

        except ValueError as e:
            print(e)


def main():
    print(1)
    print("""
    input function number:
    1. linear
    2. quadratic
    3. sinus
    """)
    menu()


if __name__ == "__main__":
    main()
