import random

def two():
    print("zad 2: wylosuj liczbe i sprawdz do ktorego przedzialu nalezy")

    rand_int = random.randint(-50, 50)
    range_one = [-50, -26]
    range_two = [-25, 0]
    range_three = [0, 24]
    range_four = [25, 50]

    print(rand_int)

    if -50 <= rand_int < -25:
        print("P1")
    elif rand_int < 0:
        print("P2")
    elif rand_int < 25:
        print("p3")
    elif rand_int <= 50:
        print('p4')
    else:
        print('error')


