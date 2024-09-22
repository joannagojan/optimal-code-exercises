

# 5. Załóżmy, że mamy funkcję f(x) = 2*x ^ 2 - 10 * x + 2. Pobierz od użytkownika wartość
# zmiennoprzecinkową do zmiennej x i wyznacz dla niej wartość funkcji f(x).

def two_five():

    print("5. Załóżmy, że mamy funkcję f(x) = 2*x ^ 2 - 10 * x + 2. Pobierz od użytkownika wartość zmiennoprzecinkową do zmiennej x i wyznacz dla niej wartość funkcji f(x).")

    draw = uniform(1.0, 100.0)

    def given_function(draw : float) -> float:
        return (2 * draw * draw) - (10 * draw) + 2

    print(f"draw: {draw}, result {given_function(draw)}")
