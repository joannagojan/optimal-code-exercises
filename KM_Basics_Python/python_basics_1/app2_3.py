
# 3. Wylosuj 3 liczby całkowite z przedziału [10, 30]. Znajdź najwiekszą oraz najmniejszą spośród
# tych liczb i sprawdź, czy ich średnia arytmetyczna jest większa od liczby, która ma środkową
# wartość.

def two_three():
    print("3. Wylosuj 3 liczby całkowite z przedziału [10, 30]. Znajdź najwiekszą oraz najmniejszą spośród tych liczb i sprawdź, czy ich średnia arytmetyczna jest większa od liczby, która ma środkową wartość.")


    def draw() -> int:
        random_int = randint(10, 30)
        return random_int

    smallest = draw()

    if (helper := draw()) <= smallest:
        middle, smallest = smallest, helper
    else:
        middle = helper

    if (helper := draw()) >= middle:
        biggest = helper
    else: # helper < middle
        if helper <= smallest: # helper najmniejszy
          biggest, middle, smallest = middle, smallest, helper
        else : # helper jest middle
            biggest, middle, smallest = middle, helper, smallest



    avg = (smallest + biggest) / 2

    print(f"{smallest, middle, biggest, avg}")
    print("equal" if avg == middle else ("avg bigger" if avg > middle else "avg smaller"))

