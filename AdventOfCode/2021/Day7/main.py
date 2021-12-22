
file = open('file.txt')
data = [int(x) for x in file.readline().split(',')]

ret = {}
maximum = max(data) + 1
for i in range(maximum):
    ret[i] = 0
    for val in data:
        ret[i] += (abs(val - i))/ 2 * (abs(val - i) + 1)

print(min(ret.values()))