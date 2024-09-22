"""
2. Napisz higher order function, która przyjmuje jako argument dwie liczby całkowite. Załóżmy, że są one reprezentowane
przez parametry a oraz b. Jako trzeci argument przyjmuje referencję do funkcji typu Callable[[int], int]. Zwróć
sumę wartości tej funkcji dla przedziału liczb [a, b] z krokiem 1.
Przykładowa sygnatura funkcji: sum_values(a: int, b: int, fn: Callable[[int], int]).
Jeżeli a = 2, b = 4 a fn to lambda x: 2 * x, wynikiem jest fn(2) + fn(3) + fn(4) czyli 2 * 2 + 2 * 3 + 2 * 4
"""


