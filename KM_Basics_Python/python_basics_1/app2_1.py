
#    1. Pobierz od użytkownika dwie liczby całkowite i wypisz większą z nich.

def two_one():
    print("1. Pobierz od użytkownika dwie liczby całkowite i wypisz większą z nich.")
    int_one = int(input("podaj pierwsza liczbe: "))
    int_two = int(input("podaj pierwsza liczbe: "))

    print("equal" if int_one == int_two else (int_one if int_one > int_two else int_two))
