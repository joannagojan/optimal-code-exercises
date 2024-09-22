
# Pobierz od użytkownika wartość – liczbę zmiennoprzecinkową, którą przechowasz o nazwie x.
# Dla pobranej wartości wyznacz wartość wielomianu 𝑊(𝑥)= 2𝑥12+3𝑥5−4𝑥2.

def two_add1():
    print("Pobierz od użytkownika wartość – liczbę zmiennoprzecinkową, którą przechowasz o nazwie x. Dla pobranej wartości wyznacz wartość wielomianu 𝑊(𝑥)= 2𝑥12+3𝑥5−4𝑥2.")

    x = float(input("podaj float: \n"))
    result = 2 * x ** 12 + 3 * x ** 5 - 4 * x ** 2
    print(result)

# Wylosuj do zmiennej a liczbę z przedziału <1,20>. Pobieraj od użytkownika dwie liczby,
# dopóki ich średnia arytmetyczna nie będzie różniła się od wartości zmiennej a o mniej
# niż 2
