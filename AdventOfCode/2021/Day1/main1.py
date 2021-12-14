val = -1
old_val = -1
counter = 0
file = open('file.txt')
while True:
    val = file.readline()
    if not val:
        break
    val = int(val)
    if old_val != -1:
        if val > old_val:
            counter += 1
    old_val = val
    
print(counter)