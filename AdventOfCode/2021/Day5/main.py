import re

max_val = 990
grid = [[0 for _ in range(max_val)] for _ in range(max_val)]

file = open('file.txt')

while True:
    line = file.readline()
    if not line:
        break
    num = re.findall(r'(\d+),(\d+) -> (\d+),(\d+)', line)[0]
    x = [int(x) for x in num]
    if x[0] == x[2]:
        for i in range(min(x[1], x[3]), max(x[1], x[3]) + 1):
            grid[x[0]][i] += 1
    elif x[1] == x[3]:
        for i in range(min(x[0], x[2]), max(x[0], x[2]) + 1):
            grid[i][x[1]] += 1
    else:
        sx = 1 if x[0] < x[2] else -1
        sy = 1 if x[1] < x[3] else -1
        for (i, j) in zip(range(x[0], x[2] + sx, sx), range(x[1], x[3] + sy, sy)):
            grid[i][j] += 1
        pass
    
coutner = 0

for i in grid:
    for j in i:
        if j >= 2:
            coutner += 1
            
print(coutner)
