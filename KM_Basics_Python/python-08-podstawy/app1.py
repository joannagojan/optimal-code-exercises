"""
Write a function that takes a string as an argument and checks how many characters
in that string have an even ASCII code.
Ensure flexibility and universality of the code by using a Higher-Order Function
"""
from typing import Callable


def is_even(number: int) -> bool:
    return number % 2 == 0


def check_ascii_for_condition(evaluated_string: str, condition: Callable[[int], bool]) -> int:
    ascii_chars = [ord(char) for char in list(evaluated_string)]
    return sum (1 for char in ascii_chars if (condition(char)))


def main() -> None:
    print(check_ascii_for_condition("Joanna", is_even))

if __name__ == "__main__":
    main()