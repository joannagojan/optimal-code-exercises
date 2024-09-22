"""
Napisz funkcję, która przyjmuje jako argument liczbę i zwraca cyfrę na wybranej pozycji w tej liczbie.
"""


def digit_at_position(number: int, position: int) -> int:

    if len(str(number)) < position <= 0:
        raise ValueError('the position is out of scope')
    if (number >= 0):
        return int(str(number)[position-1])
    else:
        return int(str(number)[position])


def main() -> None:
    try:
        print(digit_at_position(63427, 1))
        print(digit_at_position(-56, 1))
        print(digit_at_position(0, 1))
    except (ValueError) as e:
        print(e)


if __name__ == "__main__":
    main()
