
file = open('file.txt')
data = [x.strip().split('|') for x in file.readlines()]

def getKey(items, value):
    for (x, y) in items:
        if value == y:
            return x

sum = 0
for val in data:
    uniq = {c: set() for c in range(10)}
    input = val[0]
    output = val[1]
    output = output.strip().split(' ')
    input = input.strip().split(' ')
    for i in input:
        if len(i) == 2:
            uniq[1] = set(i)
        if len(i) == 4:
            uniq[4] = set(i)
        if len(i) == 7:
            uniq[8] = set(i)
        if len(i) == 3:
            uniq[7] = set(i)
    for i in input:
        if (len(i) == 6) and (uniq[4].issubset(set(i))):
            uniq[9] = set(i)
        if (len(i) == 5) and (uniq[7].issubset(set(i))):
            uniq[3] = set(i)
        if (len(i) == 5) and (len(uniq[4] - set(i)) == 2):
            uniq[2] = set(i)
    for i in input:
        if (len(i) == 6) and (set(i) != uniq[9]) and (uniq[7].issubset(set(i))):
            uniq[0] = set(i)
        if (len(i) == 5) and (set(i) != uniq[3]) and (len(uniq[4] - set(i)) == 1):
            uniq[5] = set(i) 
    for i in input:
        if not (set(i) in uniq.values()):
            uniq[6] = set(i)
    num = '';
    for out in output:
        num = num + str(getKey(uniq.items(), set(out)));
    sum += int(num)
    
print(sum)
    
            
            