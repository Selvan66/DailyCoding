def main():
    with open("data.txt") as file:
        stacks = [["V", "J", "B", "D"],
                  ["F", "D", "R", "W", "B", "V", "P"],
                  ["Q", "W", "C", "D", "L", "F", "G", "R"],
                  ["B", "D", "N", "L", "M", "P", "J", "W"],
                  ["Q", "S", "C", "P", "B", "N", "H"],
                  ["G", "N", "S", "B", "D", "R"],
                  ["H", "S", "F", "Q", "M", "P", "B", "Z"],
                  ["F", "L", "W"],
                  ["R", "M", "F", "V", "S"]]
        is_moves = False
        for line in file.readlines():
            line = line.rstrip()

            if line == "":
                is_moves = True
                continue
            elif not is_moves:
                continue

            splited = line.split()
            (number, stack_from, stack_to) = (
                int(splited[1]), int(splited[3]) - 1, int(splited[5]) - 1)

            for _ in range(number):
                value = stacks[stack_from].pop(0)
                stacks[stack_to].insert(0, value)
        print([x[0] for x in stacks])


if __name__ == "__main__":
    main()
