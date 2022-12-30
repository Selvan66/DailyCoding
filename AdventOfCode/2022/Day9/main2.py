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
        snake = [[0, 0] for _ in range(10)]
        for line in file.readlines():
            line = line.rstrip()
            (d, m) = line.split(" ")
            m = int(m)
            for _ in range(m):
                match d:
                    case "R": snake[0][0] += 1
                    case "L": snake[0][0] -= 1
                    case "U": snake[0][1] += 1
                    case "D": snake[0][1] -= 1

                for i in range(1, 10):
                    move_to_head(snake[i - 1], snake[i],
                                 tail_pos if i == 9 else set())
        print(len(tail_pos))


if __name__ == "__main__":
    main()
