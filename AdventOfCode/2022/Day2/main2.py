
def main():
    point = 0
    with open("data.txt") as file:
        for line in file.readlines():
            line = line.rstrip()
            fight = line.split(" ")
            oponent = fight[0]
            you = fight[1]
            match (oponent, you):
                case ("A", "X"): point += 0 + 3
                case ("A", "Y"): point += 3 + 1
                case ("A", "Z"): point += 6 + 2
                case ("B", "X"): point += 0 + 1
                case ("B", "Y"): point += 3 + 2
                case ("B", "Z"): point += 6 + 3
                case ("C", "X"): point += 0 + 2
                case ("C", "Y"): point += 3 + 3
                case ("C", "Z"): point += 6 + 1
    print(point)


if __name__ == "__main__":
    main()
