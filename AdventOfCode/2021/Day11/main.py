file = open('file.txt')
data = []
for line in file.readlines():
    data.append([int(x) for x in line if x != '\n'])

def increase_energy():
    for y in range(len(data)):
        for x in range(len(data[0])):
            data[x][y] += 1

def flash_neig(x, y):
    if (x + 1 < len(data)) and (data[x + 1][y] != 0):
        data[x + 1][y] += 1
    if (x + 1 < len(data)) and (y + 1 < len(data)) and (data[x + 1][y + 1] != 0):
        data[x + 1][y + 1] += 1
    if (x + 1 < len(data)) and (y - 1 >= 0) and (data[x + 1][y - 1] != 0):
        data[x + 1][y - 1] += 1
    if (x - 1 >= 0) and (data[x - 1][y] != 0):
        data[x - 1][y] += 1
    if (x - 1 >= 0) and (y + 1 < len(data)) and (data[x - 1][y + 1] != 0):
        data[x - 1][y + 1] += 1
    if (x - 1 >= 0) and (y - 1 >= 0) and (data[x - 1][y - 1] != 0):
        data[x - 1][y - 1] += 1
    if (y + 1 < len(data)) and (data[x][y + 1] != 0):
        data[x][y + 1] += 1
    if (y - 1 >= 0) and (data[x][y - 1] != 0):
        data[x][y - 1] += 1
        
def flash():
    sum = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[x][y] > 9:
                sum += 1
                data[x][y] = 0
                flash_neig(x, y)
                         
    return sum
                
def step():
    sum = 0
    increase_energy()
    value = flash()
    sum += value
    while value > 0:
        value = flash()
        sum += value

    return sum


sum = 0
i = 0
while sum != 100:
    sum = step()
    i += 1
print(data)
print(i)