
def parse_line(line: str):
    mods = line.split(" ")
    mod = mods[0]
    ranges = mods[1].split(",")
    x = ranges[0].split("=")[1].split("..")
    y = ranges[1].split("=")[1].split("..")
    z = ranges[2].split("=")[1].split("..")
    x = [int(x[0]), int(x[1])]
    y = [int(y[0]), int(y[1])]
    z = [int(z[0]), int(z[1])]

    return (mod == "on", x, y, z)


def flat_range(range: list):
    result = []
    stack = list(sorted(range))
    if len(stack) < 2:
        return stack
    r = stack.pop(0)
    nr = stack.pop(0)
    while len(stack) != 0:
        print(stack)
        if r[1] == nr[0]:
            a = [r[0], nr[1]]
            r = a
        else:
            result.append(r)
            r = nr
        nr = stack.pop(0)

    if r[1] == nr[0]:
        result.append([r[0], nr[1]])
    else:
        result.append(r)
        result.append(nr)
    return result


def add_range(range1: list, range2: list):
    result = []
    if len(range1) == 0:
        return [range2]
    elif len(range1) == 1:
        r = range1[0]
        if r[0] > range2[0]:
            if range2[1] <= r[0]:
                result.append(range2)
                result.append(r)
            else:
                result.append([range2[0], r[1]])
        else:
            if r[1] >= range2[0]:
                result.append([r[0], range2[1]])
            else:
                result.append(r)
                result.append(range2)
        return result
    stack = range1

    r = stack.pop(0)
    if r[0] > range2[0]:
        if range[1] <= r[0]:
            result.append(range2)
        else:
            result.append([range2[0], r[1]])

    nr = stack.pop(0)
    while len(stack) != 0:
        if r[1] <= range2[0]:
            result.append([r[0], range2[1]])
            nr[0] = range2[1]
        elif r[1] > range2[0]:
            result.append(r)
        r = nr
        nr = stack.pop(0)
    return result


def sub_range(range1: list, range2: list):
    result = []
    stack = list(sorted(range1 + range2))
    if len(stack) < 2:
        return stack
    print(stack)
    r = stack.pop(0)
    nr = stack.pop(0)
    while len(stack) != 0:
        if r[1] <= nr[0]:
            result.append(r)
        elif r[1] > nr[0]:
            result.append(r)
            nr[0] = r[1]
        r = nr
        nr = stack.pop(0)

    if r[1] <= nr[0]:
        result.append(r)
    elif r[1] > nr[0]:
        result.append(r)
        nr[0] = r[1]
    result.append(nr)
    return result


def main():
    xrange = []
    a = add_range(xrange, [2, 4])
    print(a)
    a = add_range(a, [1, 3])
    print(a)
    a = add_range(a, [5, 7])
    a = add_range(a, [3, 8])
    print(a)
    yrange = []

    zrange = []
    with open("data.txt") as file:
        for line in file.readlines():
            (mod, x, y, z) = parse_line(line.strip())


if __name__ == '__main__':
    main()
