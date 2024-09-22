# 2. Napisz funkcję, która przyjmuje jako argument dwa napisy. Będzie to imię i nazwisko. Funkcja zwraca napis
# wielowierszowy, który jest postaci:
# """
# Twoje imię to: ...
# Twoje nazwisko to: ...
# """


def get_introduction(name: str, surname: str):
    return f'"""\n Your name is: {name}\n You surname is: {surname}\n"""'


print(get_introduction('asia', 'gojan'))