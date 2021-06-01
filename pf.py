from collections import deque


def path_finder(maze):
    table = list(map(list, maze.split("\n")))
    nm = len(table[0]) - 1  # max x and y
    fc = deque()  # free cords.
    fc.append([0, 0])  # start from

    while fc:  # trying find exit while has free x and y
        element = fc.pop()

        x = element[1]
        y = element[0]

        print(x, y)

        if element == [nm, nm]:
            return True

        if table[y][x] == 'C':  # checked?
            continue

        # go right
        if nm >= y and nm >= x + 1 and table[y][x + 1] == '.' and table[y][x + 1] != 'C':
            fc.appendleft([y, x + 1])

        # go down
        if nm >= y + 1 and nm >= x and table[y + 1][x] == '.' and table[y + 1][x] != 'C':
            fc.appendleft([y + 1, x])

        # go up
        if y - 1 >= 0 and x >= 0 and table[y - 1][x] == '.' and table[y - 1][x] != 'C':
            fc.appendleft([y - 1, x])

        # go left
        if y >= 0 and x - 1 >= 0 and table[y][x - 1] == '.' and table[y][x - 1] != 'C':
            fc.appendleft([y, x - 1])

        table[y][x] = 'C'

    return False
