def find_min_route(tsp):
    sums = 0
    counter = 0
    j = 0
    i = 0
    mins = 2147483647
    visited_route_list = [0]
    route = [0] * len(tsp)

    while(i < len(tsp) and j < len(tsp[i])):
            if counter >= len(tsp[i]) - 1: break

            if (j != i and (j not in visited_route_list)):
                if (tsp[i][j] < mins):
                    mins = tsp[i][j]
                    route[counter] = j + 1

            j = j + 1

            if (j == len(tsp[i])):
                sums = sums + mins
                mins = 2147483647
                visited_route_list.append(route[counter] - 1)
                j = 0
                i = route[counter] - 1
                counter = counter + 1

    i = route[counter - 1] - 1
    for j in range(len(tsp)):
        if (i != j and tsp[i][j] < mins):
            mins = tsp[i][j]
            route[counter] = j + 1

    sums = sums + mins

    print('Minimum cost is: ')
    print(sums)


def main():
    tsp = [
        [-1, 10, 15, 20],
        [10, -1, 35, 25],
        [15, 35, -1, 30],
        [20, 25, 30, -1]
    ]

    find_min_route(tsp)


main()
