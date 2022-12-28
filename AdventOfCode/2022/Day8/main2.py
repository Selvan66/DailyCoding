
def main():
    with open("data.txt") as file:
        grid = []
        for line in file.readlines():
            line = line.rstrip()
            grid.append([int(x) for x in line])

        height = len(grid)
        width = len(grid[0])
        max_eaves = 0
        for i in range(1, height - 1):
            for j in range(1, width - 1):
                dis = [0 for _ in range(4)]

                for m in range(1, i + 1):
                    if grid[i][j] > grid[i - m][j]:
                        dis[0] += 1
                    else:
                        dis[0] += 1
                        break
                for m in range(1, height - i):
                    if grid[i][j] > grid[i + m][j]:
                        dis[1] += 1
                    else:
                        dis[1] += 1
                        break
                for m in range(1, j + 1):
                    if grid[i][j] > grid[i][j - m]:
                        dis[2] += 1
                    else:
                        dis[2] += 1
                        break
                for m in range(1, width - j):
                    if grid[i][j] > grid[i][j + m]:
                        dis[3] += 1
                    else:
                        dis[3] += 1
                        break
                eaves = dis[0] * dis[1] * dis[2] * dis[3]
                max_eaves = max(max_eaves, eaves)
        print(max_eaves)


if __name__ == "__main__":
    main()
