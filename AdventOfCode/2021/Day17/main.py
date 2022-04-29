
topleft = (209, -59)
bottomright = (238, -86)

def isOutside(x, y):
    return x > bottomright[0] or y < bottomright[1]

def isInside(x, y):
    return (topleft[0] <= x <= bottomright[0]) and (topleft[1] >= y >= bottomright[1])

minx = 21
maxx = 50
isin = set()
for i in range(0, 600):
    for j in range(-87, 1000):
        y = 0
        x = 0
        vx = i
        vy = j
        while not isOutside(x, y):
            x = x + vx
            y = y + vy
            if vx > 0:
                vx = vx - 1
            elif vx < 0:
                vx = vx + 1
            vy = vy - 1
            if isInside(x, y):
                isin.add((i, j))

print(len(isin))