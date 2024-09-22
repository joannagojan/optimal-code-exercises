

# 2. Pobierz od użytkownika dwie liczby całkowite i sprawdź, czy ich suma jest większa od liczby
# wylosowanej z przedziału [10, 30].

def two_two():
    print(" 2. Pobierz od użytkownika dwie liczby całkowite i sprawdź, czy ich suma jest większa od liczby wylosowanej z przedziału [10, 30].")
    input_one = int(input("Podaj pierwsza liczbe calkowita: "))
    input_two = int(input("Podaj druga liczbe calkowita: "))

    random_int = randint(10, 30)
    input_sum = input_one+input_two

    print(f'sum: {input_sum}, random: {random_int}')
    print("equal" if input_sum==random_int else("bigger" if input_sum > random_int else "smaller" ))