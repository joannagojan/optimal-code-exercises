"""
Write a function that checks whether the string passed as an argument is a palindrome.
"""


def is_palindrome(evaluated: str) -> bool:
    return evaluated == evaluated[::-1]

def main() -> None:
    print(is_palindrome("kajak"))
    print(is_palindrome("kajjak"))
    print(is_palindrome("hello"))

if __name__ == "__main__":
    main()