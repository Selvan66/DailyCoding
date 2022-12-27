
def main():
    with open("data.txt") as file:
        grid = []
        for line in file.readlines():
            line = line.rstrip()
            grid.append([int(x) for x in line])

        height = len(grid)
        width = len(grid[0])
        num_of_vis = 0
        for i in range(1, height - 1):
            for j in range(1, width - 1):
                vis = [True for _ in range(4)]
                for m in range(0, i):
                    if grid[i][j] <= grid[m][j]:
                        vis[0] = False
                for m in range(i + 1, height):
                    if grid[i][j] <= grid[m][j]:
                        vis[1] = False
                for m in range(0, j):
                    if grid[i][j] <= grid[i][m]:
                        vis[2] = False
                for m in range(j + 1, width):
                    if grid[i][j] <= grid[i][m]:
                        vis[3] = False
                if any(vis):
                    num_of_vis += 1

        num_of_vis += 2*height + 2*width - 4
        print(num_of_vis)


if __name__ == "__main__":
    main()
