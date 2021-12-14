command = ''
val = 0
depth = 0
horizontal = 0
aim = 0
file = open('file.txt')
while True:
    line = file.readline()
    if not line:
        break
    [command, val] = line.split(' ')
    val = int(val)
    if command == 'forward':
        horizontal += val
        depth += (val * aim)
    if command == 'down':
        aim += val
    if command == 'up':
        aim -= val

print(depth, horizontal, depth * horizontal)