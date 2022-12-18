def main():
    with open("data.txt") as file:
        sum = 0
        for line in file.readlines():
            line = line.rstrip()
            size = len(line) // 2
            lhs = set(line[:size])
            rhs = set(line[size:])
            char = lhs.intersection(rhs).pop()
            value = 0
            if char.isupper():
                value = ord(char) - ord('A') + 27
            else:
                value = ord(char) - ord('a') + 1
            sum += value
        print(sum)


if __name__ == "__main__":
    main()
