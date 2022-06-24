# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

""" i1 = co[0]
    j1 = co[1]
    m1 = co[2]
    n1 = co[3]
    found = False
    for s in ALL_SQUARES:
        if s[(i1 - 1) // 4][(i1 - 1) % 4] != square[(i1 - 1) // 4][(i1 - 1) % 4] or s[(j1 - 1) // 4][(j1 - 1) % 4] != \
                square[(j1 - 1) // 4][(j1 - 1) % 4] or s[(m1 - 1) // 4][(m1 - 1) % 4] != square[(m1 - 1) // 4][
                (m1 - 1) % 4] or s[(n1 - 1) // 4][(n1 - 1) % 4] != square[(n1 - 1) // 4][(n1 - 1) % 4]:
            found = True
        if found:
            return "UNIQUE" + " ".join(str(x) for x in co)
        else:
            return "-" """


def check_square(co, s):
    i1 = co[0]
    j1 = co[1]
    m1 = co[2]
    n1 = co[3]
    if s[(i1 - 1) // 4][(i1 - 1) % 4] != square[(i1 - 1) // 4][(i1 - 1) % 4] or s[(j1 - 1) // 4][(j1 - 1) % 4] != \
            square[(j1 - 1) // 4][(j1 - 1) % 4] or s[(m1 - 1) // 4][(m1 - 1) % 4] != square[(m1 - 1) // 4][
        (m1 - 1) % 4] or s[(n1 - 1) // 4][(n1 - 1) % 4] != square[(n1 - 1) // 4][(n1 - 1) % 4]:
        return False # если не найден, то вернет это
    else:
        return True # если найден, то это


def check(co):
    co = co
    found = False # если хотя бы раз найден, то уже не уникален
    for s in ALL_SQUARES:
        if not found:
            found = check_square(co, s)
        else:
            break

    return found



# first square
square = [["A", "B", "C", "D"], ["B", "A", "D", "C"], ["C", "D", "A", "B"], ["D", "C", "B", "A"]]

ALL_SQUARES = [
    # second square
    [["A", "B", "C", "D"], ["B", "A", "D", "C"], ["C", "D", "B", "A"], ["D", "C", "A", "B"]],
    # third square
    [["A", "B", "C", "D"], ["B", "A", "D", "C"], ["D", "C", "A", "B"], ["C", "D", "B", "A"]],
    # forth square
    [["A", "B", "C", "D"], ["B", "A", "D", "C"], ["D", "C", "B", "A"], ["C", "D", "A", "B"]],
    # fifth square
    [["A", "B", "C", "D"], ["B", "C", "D", "A"], ["C", "D", "A", "B"], ["D", "A", "B", "C"]],
    # sixth square
    [["A", "B", "C", "D"], ["B", "C", "D", "A"], ["D", "A", "B", "C"], ["C", "D", "A", "B"]],
    # seventh square
    [["A", "B", "C", "D"], ["B", "D", "A", "C"], ["C", "A", "D", "B"], ["D", "C", "B", "A"]],
    # eighth square
    [["A", "B", "C", "D"], ["B", "D", "A", "C"], ["D", "C", "B", "A"], ["C", "A", "D", "B"]],
    # ninth square
    [["A", "B", "C", "D"], ["C", "A", "D", "B"], ["B", "D", "A", "C"], ["D", "C", "B", "A"]],
    # tenth square
    [["A", "B", "C", "D"], ["C", "A", "D", "B"], ["D", "C", "B", "A"], ["B", "D", "A", "C"]],
    # eleventh square
    [["A", "B", "C", "D"], ["C", "D", "A", "B"], ["B", "A", "D", "C"], ["D", "C", "B", "A"]],
    # twelfth square
    [["A", "B", "C", "D"], ["C", "D", "A", "B"], ["B", "C", "D", "A"], ["D", "A", "B", "C"]],
    # thirteenth
    [["A", "B", "C", "D"], ["C", "D", "A", "B"], ["D", "A", "B", "C"], ["B", "C", "D", "A"]],
    # fourteenth
    [["A", "B", "C", "D"], ["C", "D", "A", "B"], ["D", "C", "B", "A"], ["B", "A", "D", "C"]],
    # fifteenth
    [["A", "B", "C", "D"], ["C", "D", "B", "A"], ["B", "A", "D", "C"], ["D", "C", "A", "B"]],
    # sixteenth
    [["A", "B", "C", "D"], ["C", "D", "B", "A"], ["D", "C", "A", "B"], ["B", "A", "D", "C"]],
    # seventeenth
    [["A", "B", "C", "D"], ["D", "A", "B", "C"], ["B", "C", "D", "A"], ["C", "D", "A", "B"]],
    # eighteenth
    [["A", "B", "C", "D"], ["D", "A", "B", "C"], ["C", "D", "A", "B"], ["B", "C", "D", "A"]],
    # nineteenth
    [["A", "B", "C", "D"], ["D", "C", "A", "B"], ["B", "A", "D", "C"], ["C", "D", "B", "A"]],
    # twentieth
    [["A", "B", "C", "D"], ["D", "C", "A", "B"], ["C", "D", "B", "A"], ["B", "A", "D", "C"]],
    # twenty-first
    [["A", "B", "C", "D"], ["D", "C", "B", "A"], ["B", "A", "D", "C"], ["C", "D", "A", "B"]],
    # twenty-second
    [["A", "B", "C", "D"], ["D", "C", "B", "A"], ["B", "D", "A", "C"], ["C", "A", "D", "B"]],
    # twenty-third
    [["A", "B", "C", "D"], ["D", "C", "B", "A"], ["C", "A", "D", "B"], ["B", "D", "A", "C"]],
    # twenty-forth
    [["A", "B", "C", "D"], ["D", "C", "B", "A"], ["C", "D", "A", "B"], ["B", "A", "D", "C"]]
]

coordinates = [0, 0, 0, 0]
UNIQUE = set()

for i in range(1, 16):
    coordinates[0] = i
    for j in range(1, 16):
        if j != i:
            coordinates[1] = j
            for m in range(1, 16):
                if (m != i) and (m != j):
                    coordinates[2] = m
                    for n in range(1, 16):
                        if (n != i) and (n != j) and (n != m):
                            coordinates[3] = n
                            if not check(coordinates):
                                UNIQUE.add(" ".join(str(x) for x in sorted(coordinates)))

UNIQUE = list(UNIQUE)

for x in sorted(UNIQUE):
    print(x)

print(len(UNIQUE))