"""
2. Napisz funkcję, która przyjmuje jako argument 2 liczby zmiennoprzecinkowe - boki prostokąta
i zwraca dwie wartości: pole i obwód prostokąta.
"""

def calculate_rectangle_area_and_perimeter(x: float, y: float) -> tuple[float, float]:


    if x <= 0 or y <= 0:
        raise ValueError("Sides cannot be non positive")
    area = x * y
    perimeter = 2 * (x + y)

    return area, perimeter


def main() -> None:
    try:
        print(calculate_rectangle_area_and_perimeter(20, 50))
        print(calculate_rectangle_area_and_perimeter(1, 2))
        print(calculate_rectangle_area_and_perimeter(-1, 2))
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()