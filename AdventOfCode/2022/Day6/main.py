def main():
    with open("data.txt") as file:
        for line in file.readlines():
            queue = []
            result = None
            for i, letter in enumerate(line):
                if i < 4:
                    queue.append(letter)
                    continue

                count = set(queue)
                if len(count) > 3:
                    result = i
                    break

                queue.append(letter)
                queue.pop(0)
            print(count, result)


if __name__ == "__main__":
    main()
