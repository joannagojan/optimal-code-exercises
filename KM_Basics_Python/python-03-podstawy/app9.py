"""
Wylosuj dwie liczby całkowite z przedziału [100, 999] oraz oblicz ich średnią arytmetyczną.
"""

import random


def draw_random_int(min_range: int, max_range: int) -> int:
    return random.randint(min_range, max_range)


def average(a: int, b: int) -> float:
    return (a + b) / 2

def main() -> None:
    print(average(int1 := draw_random_int(100, 999), int2 := draw_random_int(100, 999)), int1, int2)

if __name__ == '__main__':
    main()