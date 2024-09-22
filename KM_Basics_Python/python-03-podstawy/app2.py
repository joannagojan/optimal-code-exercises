"""
Write a function that takes 3 floating-point
numbers as arguments and checks if they can be the sides of an equilateral triangle
"""

def validate_equilateral_triangle_sides(a: float, b: float, c: float) -> bool:

    for arg in (a,b,c):
        if not isinstance(arg, float):
            raise TypeError("not a float")
        elif arg <= 0:
            raise ValueError("cannot be smaller than 0")

    if a == b and b == c:
        return True
    else:
        return False

def main():


    try:
        # print(validate_equilateral_triangle_sides("hg", -3, 5))
        # print(validate_equilateral_triangle_sides4,5,6))
        # print(validate_equilateral_triangle_sides(-4.7,4.7,4.7))
        print(validate_equilateral_triangle_sides(4.7,4.7,4.7))


    except (ValueError, TypeError) as error:
        print(error)



if __name__ == '__main__':
    main()

