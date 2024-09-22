"""
Napisz higher order function, która przyjmuje jako argument dwie liczby całkowite oraz referencję do funkcji
jako trzeci argument. Funkcja przekazywana jako trzeci argument ma typ Callable[[int, int], int] i określa operację,
którą należy wykonać na dwóch pierwszych argumentach higher order function. Higher order function zwraca podwoją
wartość wyniku tej operacji.
"""

from typing import Callable


def double_results(x: int, y: int, funct: Callable[[int, int], int]) -> int:
    return 2 * funct(x, y)


def sum_numbers(a: int, b: int) -> int:
    return a + b


def main() -> None:
    print(double_results(4, 10, sum_numbers))


if __name__ == '__main__':
    main()
