
def two_add10():
    print("Wylosuj do zmiennej a liczbę z przedziału <1,20>. Pobieraj od użytkownika dwie liczby, dopóki ich średnia arytmetyczna nie będzie różniła się od wartości zmiennej a o mniej niż 2")

    a = randint(1,20)

    def get_input()-> tuple[int, int]:
        inp_one = int(input("Podaj liczbe 1: "))
        inp_two = int(input("podaj liczbe 2: "))
        print(a, inp_one, inp_two, "abs:", abs((inp_one + inp_two) / 2 -a))
        return inp_one, inp_two

    inp_one, inp_two = get_input()

    while abs((inp_one + inp_two) / 2 -a) >= 2:
        inp_one, inp_two = get_input()

    print(a, inp_one, inp_two, "abs:" , abs((inp_one + inp_two) / 2 -a))
