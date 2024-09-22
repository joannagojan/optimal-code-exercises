

# 4. Wylosuj 2 liczby zmiennoprzecinkowe. Będą to boki prostokąta. Oblicz pole i obwód tego
# prostokąta.

def two_four():
    print("# 4. Wylosuj 2 liczby zmiennoprzecinkowe. Będą to boki prostokąta. Oblicz pole i obwód tego prostokąta.")

    side_one = uniform(0.1, 99.99)
    side_two = uniform(0.1, 99.99)

    area = side_one * side_two
    peri = 2*(side_one+side_two)

    print(f"side 1: {side_one}, side_two: {side_two}, area: {area}, perimeter: {peri}")