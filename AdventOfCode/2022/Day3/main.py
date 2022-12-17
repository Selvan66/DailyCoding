def main():
    with open("data.txt") as file:
        sum = 0
        i = 0
        group = []
        for line in file.readlines():
            line = line.rstrip()
            group.append(line)
            i += 1
            if i == 3:
                all_set = None
                for line in group:
                    if all_set == None:
                        all_set = set(line)
                    else:
                        all_set = all_set.intersection(set(line))
                char = all_set.pop()
                value = 0
                if char.isupper():
                    value = ord(char) - ord('A') + 27
                else:
                    value = ord(char) - ord('a') + 1
                sum += value

                i = 0
                group.clear()
        print(sum)


if __name__ == "__main__":
    main()
