# 3. Napisz kalkulator figur, w którym wybierasz figurę, np.
# a. kwadrat
# b. prostokat
# c. trojkat rownoboczny
# d. trapez rownoramienny
# Nastepnie uzytkownika podaje potrzebne długości boków i wypisujesz pole i obwód figury.


def three_three() -> dict[str : int]:

    # dict = {figure: [edge1, edge2, perimeter, area]}
    result_dict = {}

    def input_edge() -> list[int]:
        edges = []
        while len(edges) < 2:
            try:
                edge = int(input("give edge, bigger than 0: \n"))
                if edge < 0:
                    print('Edges cannot be smaller or equal 0')
                else:
                    edges.append(int(edge))
                    print(edges)
            except ValueError:
                print('incorrect type, try again')
        return edges


    while True:
        user_input = input("Input a, b, c, d, or q to quit: \n")
        input_edge()

        match user_input:
            case "a": #square

                pass


            case "q":
                break


    return

three_three()
