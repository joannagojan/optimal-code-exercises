"""
Write a function that takes the x and y coordinates of a point on a plane
as arguments and returns the distance of that point from the origin of the coordinate system.
"""
import math

def distance_from_origin(x: int, y: int) -> float:
    distance = math.sqrt(x ** 2 + y ** 2)

    return distance


def main() -> None:
    print(distance_from_origin(-4, 5))


if __name__ == '__main__':
    main()
