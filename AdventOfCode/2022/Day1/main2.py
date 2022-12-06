
def main():
    allElf = []
    sumCal = 0
    with open("data.txt") as file:
        for line in file.readlines():
            line = line.rstrip()
            if len(line) <= 0:
                allElf.append(sumCal)
                sumCal = 0
            else:
                sumCal += int(line)
    allElf.sort()
    print(allElf[-1] + allElf[-2] + allElf[-3])


if __name__ == "__main__":
    main()
