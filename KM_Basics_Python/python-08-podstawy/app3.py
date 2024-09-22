"""
Write a function that checks whether the ratio of vowels to consonants in a given string is greater than the value of ratio,
which is passed as an argument. If the ratio is 0.4 and the string is "ALADYN",
then the number of vowels is 3 and the number of consonants is 3, giving us a ratio of 3/3, which equals 1.
 This value is greater than the ratio of 0.4. In such a case, the function returns True.
"""
from typing import Callable

def input_until_cond(message: str, condition: Callable[[str], bool]) -> str:
    if not condition(x := input(f'{message} \n')):
        raise ValueError("Input again")
    else:
        return x


def calculate_ratio(x: int, y: int) -> float:
    return x / y

def count_vowels(evaluated: str) -> int:
    return sum([1 for char in list(evaluated.lower()) if char in "aeioyu"])

def count_consonants(evaluated: str) -> int:
    return sum([1 for char in list(evaluated.lower()) if char not in "aeioyu"])

def compare_to_ratio(vowel_ratio: float, ratio_compared: float) -> bool:
    return vowel_ratio > ratio_compared

def main() -> None:
    evaluated_string = input_until_cond("input string", lambda x: len(x) > 2)
    ratio_vowel_to_consonant = calculate_ratio(count_vowels(evaluated_string), count_consonants(evaluated_string))

    print(compare_to_ratio(ratio_vowel_to_consonant, 1.001))

if __name__ == "__main__":
    main()