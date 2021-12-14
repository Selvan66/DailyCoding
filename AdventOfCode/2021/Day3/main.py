file = open('file.txt')
lines = file.readlines()

ones_start = ''
zeros_start = ''

znum = ''
onum = ''

for i in range(12):
    ones = [0, 0]
    zeros = [0, 0]
    for line in lines:
        if line.startswith(ones_start):
            if line[i] == '0':
                ones[0] += 1
            else:
                ones[1] += 1
            onum = line
        if line.startswith(zeros_start):
            if line[i] == '0':
                zeros[0] += 1
            else:
                zeros[1] += 1
            znum = line
    if ones[0] != 0 and ones[1] != 0:
        if ones[1] >= ones[0]:
            ones_start = ones_start + '1'
        else:
            ones_start = ones_start + '0'
    if zeros[0] != 0 and zeros[1] != 0:
        if zeros[0] <= zeros[1]:
            zeros_start = zeros_start + '0'
        else:
            zeros_start = zeros_start + '1'

print(zeros_start, ones_start)
print(znum, onum)
print(int(znum, 2),  int(onum, 2))
print(int(znum, 2) *  int(onum, 2))