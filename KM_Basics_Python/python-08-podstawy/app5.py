"""
5. Write a function that takes two strings, n1 and n2, as arguments. If the strings have the same length,
the function returns a new string where the first letter of the new string is the first letter of n1,
and the last letter of the new string is the first letter of n2.
Then, the second letter of the new string is the second letter of n1,
 and the second-to-last letter of the new string is the second letter of n2, and so on.
When n1 = 'ABCD' and n2 = 'EFGH', the new string looks like this: ABCDHGFE.
"""
import math


def check_if_same_length(x: str, y: str) -> bool:
    return len(x) == len(y)

def mix_words(c1: str, c2: str) -> str:
    if check_if_same_length(c1, c2):
        c2_reversed = [char for char in c2[::-1]]
        return ''.join(list(c1) + c2_reversed)

    else:
        return 'not same length'


def main() -> None:
    print(mix_words('ABCD', "EFGH"))


if __name__ == "__main__":
    main()
