
    
file = open('file.txt')
data = []
size = (100, 100)
points = set()
for line in file.readlines():
    data.append([int(x) for x in line if x != '\n'])

def is_lowest_point(x, y, value):
    if (x + 1 < size[0]) and (data[x + 1][y] <= value):
        return False
    if (x - 1 >= 0) and (data[x - 1][y] <= value):
        return False
    if (y + 1 < size[1]) and (data[x][y + 1] <= value):
        return False
    if (y - 1 >= 0) and (data[x][y - 1] <= value):
        return False
    return True
        
p = set()
def get_basin(x, y):
    if data[x][y] == 9:
        return
    if not (x, y) in p:
        p.add((x, y))
    else:
        return
    if (x + 1 < size[0]):
        get_basin(x + 1, y)
    if (x - 1 >= 0):
        get_basin(x - 1, y)
    if (y + 1 < size[1]):
        get_basin(x, y + 1)
    if (y - 1 >= 0):
        get_basin(x, y - 1)
        
for x in range(0, size[0]):
    for y in range(0, size[1]):
        get_basin(x, y)
        points.add(len(p))
        p = set()
        
print(points)
print(99 * 100 * 107)