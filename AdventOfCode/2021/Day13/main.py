
points = set()
width = 0
height = 0

with open('file1.txt') as file:
    for line in file.readlines():
        p = line.split(',')
        x = int(p[0])
        y = int(p[1])
        points.add((x, y))
        if x > width:
            width = x
        if y > height:
            height = y

folds = []
with open('file2.txt') as file:
    for line in file.readlines():
        p = line.split('=')
        folds.append((p[0], int(p[1])))
                

for fold in folds:
    fold_points = set()
    if fold[0] == 'x':
        width = fold[1]
        for p in points:
            if p[0] > width:
                fold_points.add((((2 * width) - p[0]), p[1]))
            else:
                fold_points.add(p)
    elif fold[0] == 'y':
        height = fold[1]
        for p in points:
            if p[1] > height:
                fold_points.add((p[0], (2 * height) - p[1]))
            else:
                fold_points.add(p)
    points = fold_points

for i in range(0, height):
    for j in range(0, width):
        p = (j, i)
        if p in points:
            print('#', end='')
        else:
            print('.', end='')
    print()