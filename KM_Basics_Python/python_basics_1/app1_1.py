# pobierz od uzytk liczbe calkowita i sprawdz czy jest wieksza o liczby wylosowanej z przedzilu [-10, 10].
# daj komunikat czy jest wieksza czy jest mniejsza albo rowna
from random import randint

def one():
    str_input = input("podaj liczbe calkowita: ")
    int_input = int(str_input)
    random_int = randint(-10, 10)

    print(f'{int_input} > {random_int}')
    print('bigger' if(int_input > random_int) else 'smaller or equal')