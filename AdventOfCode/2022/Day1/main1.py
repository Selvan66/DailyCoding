
def main():
    maxCal = 0
    sumCal = 0
    with open("data.txt") as file:
        for line in file.readlines():
            line = line.rstrip()
            if len(line) <= 0:
                if sumCal > maxCal:
                    maxCal = sumCal
                sumCal = 0
            else:
                sumCal += int(line)
    print(maxCal)


if __name__ == "__main__":
    main()
