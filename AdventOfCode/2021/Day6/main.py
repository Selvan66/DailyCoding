
file = open('file.txt')
data = [int(x) for x in file.readline().split(',')]

fishs = {i: 0 for i in range(9)}
for val in data:
    fishs[val] += 1
    
for day in range(256):
    zero = fishs[0]
    fishs[0] = fishs[1]
    fishs[1] = fishs[2]
    fishs[2] = fishs[3]
    fishs[3] = fishs[4]
    fishs[4] = fishs[5]
    fishs[5] = fishs[6]
    fishs[6] = zero
    fishs[6] = fishs[6] + fishs[7]
    fishs[7] = fishs[8]
    fishs[8] = zero  

print(sum(fishs.values()))
