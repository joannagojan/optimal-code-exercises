"""
Write a function that takes a string as an argument and returns a new string.
In the new string, place the i-th character from the input string at the i-th position if its ASCII code is even.
Otherwise, place either the i-th character from the input string or the letter 'a' (
depending on the character's ASCII code — use the one with the higher code).
 Ensure flexibility and universality of the code by using a Higher-Order Function
"""

from typing import Callable

def is_even(number: int) -> bool:
    return number % 2 == 0

def get_bigger_int(a: int, b: int) -> int:
    return max(a, b)

def get_input_until_cond(message: str, condition: Callable[[str],bool]):
    while not condition(user_word := input(f"{message} \n")):
        pass
    else:
        return user_word


def change_char_with_condition(changed_pos: int, change_to_char: str, changed_sentence: str, cond: Callable[[int, int], int]) -> str:
    if changed_pos > len(changed_sentence) - 1:
        raise ValueError('Changed position is out of range for this string')
    changed_to_list = list(changed_sentence)
    changed_to_list[changed_pos] = chr(cond(ord(changed_to_list[changed_pos]), ord(change_to_char)))

    return ''.join(changed_to_list)

def main() -> None:
    try:
        print(change_char_with_condition(1, 'a', get_input_until_cond("give string you want to change", lambda x: len(x) > 1), get_bigger_int))
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()