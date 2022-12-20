def main():
    with open("data.txt") as file:
        all = 1000  # Size of file
        for line in file.readlines():
            line = line.rstrip()
            lhs, rhs = line.split(",")
            lhs_a, lhs_b = [int(x) for x in lhs.split("-")]
            rhs_a, rhs_b = [int(x) for x in rhs.split("-")]

            if lhs_b < rhs_a:
                all -= 1
            elif rhs_b < lhs_a:
                all -= 1
        print(all)


if __name__ == "__main__":
    main()
