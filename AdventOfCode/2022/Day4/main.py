def main():
    with open("data.txt") as file:
        num_of_lazy = 0
        for line in file.readlines():
            line = line.rstrip()
            lhs, rhs = line.split(",")
            lhs_a, lhs_b = [int(x) for x in lhs.split("-")]
            rhs_a, rhs_b = [int(x) for x in rhs.split("-")]
            if lhs_a <= rhs_a and rhs_b <= lhs_b:
                num_of_lazy += 1
            elif rhs_a <= lhs_a and lhs_b <= rhs_b:
                num_of_lazy += 1
        print(num_of_lazy)


if __name__ == "__main__":
    main()
