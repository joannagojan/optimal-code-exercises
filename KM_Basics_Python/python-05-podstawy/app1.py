"""
 Napisz funkcję, która przyjmuje jako argument 3 liczby zmiennoprzecikowe i zwraca 3 wartości:
Liczbę największą spośród 3 argumentów, liczbę najmniejszą spośród 3 podanych oraz informację, czy
liczby w podanej w argumentach kolejności tworzą ciąg arytmetyczny.
"""


def get_max_min_is_sequence(x: float, y: float, z: float) -> tuple[float, float, bool]:
    max_float = max(x, y, z)
    min_float = min(x, y, z)

    min_middle_difference = x - y
    middle_max_difference = y - z

    is_arithmetic_sequence = (min_middle_difference == middle_max_difference)
    return min_float, max_float, is_arithmetic_sequence


print(get_max_min_is_sequence(1, 2, 3))
print(get_max_min_is_sequence(4, 8, 6))
print(get_max_min_is_sequence(4, 6, 8))
print(get_max_min_is_sequence(1, 42, 33))

