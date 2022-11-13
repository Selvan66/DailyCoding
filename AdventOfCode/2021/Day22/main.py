
def parse_line(line):
    mods = line.split(" ")
    mod = mods[0]
    ranges = mods[1].split(",")
    x = ranges[0].split("=")[1].split("..")
    y = ranges[1].split("=")[1].split("..")
    z = ranges[2].split("=")[1].split("..")
    x = range(int(x[0]), int(x[1])+1)
    y = range(int(y[0]), int(y[1])+1)
    z = range(int(z[0]), int(z[1])+1)
    return (mod == "on", x, y, z)


def main():
    times = 0
    cube = [[[0 for _ in range(-50, 51)] for _ in range(-50, 51)]
            for _ in range(-50, 51)]
    with open("data.txt") as file:
        for line in file.readlines():
            (mod, x, y, z) = parse_line(line.strip())
            print(mod, x, y, z)

            for i in x:
                for j in y:
                    for k in z:
                        if mod:
                            cube[i+50][j+50][k+50] = 1
                        else:
                            cube[i+50][j+50][k+50] = 0
            times += 1
            if times == 20:
                break

    counter = 0
    for i in cube:
        for j in i:
            for k in j:
                counter += k
    print(counter)


if __name__ == '__main__':
    main()
