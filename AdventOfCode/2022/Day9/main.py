import math


def move_to_head(head, tail, tail_pos):
    while math.dist(head, tail) > math.sqrt(2) + 0.001:
        if head[0] == tail[0]:
            tail[1] += -1 if tail[1] > head[1] else 1
        elif head[1] == tail[1]:
            tail[0] += -1 if tail[0] > head[0] else 1
        else:
            tail[0] += 1 if head[0] > tail[0] else -1
            tail[1] += 1 if head[1] > tail[1] else -1
        tail_pos.add(tuple(tail))


def main():
    with open("data.txt") as file:
        tail_pos = set()
        tail_pos.add((0, 0))
        head = [0, 0]
        tail = [0, 0]
        for line in file.readlines():
            line = line.rstrip()
            (d, m) = line.split(" ")
            m = int(m)
            match d:
                case "R": head[0] += m
                case "L": head[0] -= m
                case "U": head[1] += m
                case "D": head[1] -= m

            move_to_head(head, tail, tail_pos)
        print(list(sorted(tail_pos)))
        print(len(tail_pos))


if __name__ == "__main__":
    main()
