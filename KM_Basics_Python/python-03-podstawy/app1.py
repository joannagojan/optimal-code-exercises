"""
1. Napisz funkcję, która przyjmuje jako argument 3 liczby całkowite i zwraca sumę dwóch największych.

"""


def biggest_number(x: int, y: int, z: int) -> int:

    ##### validate args #####

    if type(x) != int:
        raise TypeError("Not an integer")

    if type(y) != int:
        raise TypeError("Not an integer")

    if type(z) != int:
        raise TypeError("Not an integer")

    ##### body #####
    biggest_int = max(x, y, z)
    smallest_int = min(x, y, z)
    middle_int = x + y + z - biggest_int - smallest_int

    return biggest_int + middle_int

##### main #####

def main() -> None:
    print(biggest_number(-3, -96, 13))
    print(biggest_number(-3, -96, "gknjd"))


if __name__ == '__main__':
    main()
