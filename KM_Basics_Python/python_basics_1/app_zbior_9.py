
# Wylosuj trzy liczby z przedziału odpowiednio <0, 10>, <-13, 23>, <34, 87>. Oblicz
# średnią arytmetyczną wyznaczonych liczb i wypisz tą liczbę spośród losowanych
# wcześniej, która ma wartość najbliżej obliczonej średniej.

def two_add9():
    print("Wylosuj trzy liczby z przedziału odpowiednio <0, 10>, <-13, 23>, <34, 87>. Oblicz średnią arytmetyczną wyznaczonych liczb i wypisz tą liczbę spośród losowanych wcześniej, która ma wartość najbliżej obliczonej średniej.")

    rand_one = uniform(0,10)
    rand_two = uniform(-13,23)
    rand_three = uniform(34,87)

    avg = (rand_one + rand_two + rand_three) / 3

    def diff(number: float, average: float) -> float:
        return abs(number - average)

    diff_dict = {rand_one : diff(rand_one, avg), rand_two : diff(rand_two, avg), rand_three : diff(rand_three, avg)}
    smallest_diff = min(diff_dict.keys())

    print(rand_one, rand_two, rand_three, "avg: ", avg, smallest_diff)
    smallest_number = diff_dict.keys()[diff_dict.values() == smallest_diff]
    print(smallest_number)

    # print(f'smallest difference: {smallest_diff}, smallest number: {diff_dict[diff_dict.values() == smallest_diff]}')

two_add9()