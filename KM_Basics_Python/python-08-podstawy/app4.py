"""
4. Write a function that takes a string and two characters c1 and c2,
as well as a Callable object representing a function that checks a certain condition for a single character.
The function returns a new string in which each character from the input string that meets the condition is replaced by c1,
and each character that does not meet the condition is replaced by c2.
"""

from typing import Callable


def input_until_condition(message: str, condition: Callable[[str], bool]) -> str:
    if not condition(x := input(f"{message} \n")):
        pass
    else:
        return x


def change_char_if_condition(c1: str, c2: str, evaluated_sentence: str, condition: Callable[[str], bool]) -> str:
    return "".join([c1 if condition(char) else c2 for char in list(evaluated_sentence)])

# example of a condition
def ascii_bigger_than_100(char: str) -> bool:
    return ord(char) > 100

def main() -> None:
    print(change_char_if_condition("a", "b", "akotob", ascii_bigger_than_100))


if __name__ == "__main__":
    main()
