val = -1
val1 = -1
val2 = -1
old_sum = -1
counter = 0
file = open('file.txt')
while True:
    val = file.readline()
    if not val:
        break
    val = int(val)
    if val1 != -1 and val2 != -1:
        sum = val + val1 + val2
        if old_sum != -1:
            if sum > old_sum:
                counter += 1
        old_sum = sum
    val2 = val1
    val1 = val
    
print(counter)