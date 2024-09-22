"""
Write a function that takes a number as an argument and returns information on whether it is prime.
"""

import math

def is_prime(number: int) -> bool:
    if number < 2:
        return False
    elif number == 2 or number == 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    else:
        for n in range(3, math.ceil(math.sqrt(number))):
            if number % n == 0:
                return False
            else:
                return True



def main() -> None:
    print(is_prime(997))


if __name__ == '__main__':
    main()
