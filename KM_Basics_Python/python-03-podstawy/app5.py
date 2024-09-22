"""
5. Napisz funkcję, która przyjmuje jako argument liczbę i zwraca sumę jej cyfr.
"""


def sum_of_digits(x: int) -> int:

    sum = 0

    for digit in str(abs(x)):
        sum += int(digit)

    return sum


def main():
    print(sum_of_digits(7329))
    print(sum_of_digits(-7329))

if __name__ == '__main__':
    main()