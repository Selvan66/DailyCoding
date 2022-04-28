
from math import prod


def parseFour(s):
    i = s[0]
    s = s[1:]
    if (i == '0'):
        return s[0:4]
    else:
        return s[0:4] + parseFour(s[4:])
    
def parseIZero(s):
    l = int(s[0:15], 2)
    ret = []
    suml = 15
    while (l > 0):
        r, le = parse(s[suml :(suml + l)])
        l = l - le
        suml = suml + le
        ret.extend(r)
    return ret, suml

def parseIOne(s):
    times = int(s[0:11], 2)
    l = 11
    ret = []
    for i in range(times):
        r, le = parse(s[l:])
        l = l + le
        ret.extend(r)
    return ret, l

def parse(s):
    if ((not len(s)) or ('1' not in s)):
        return [], 0
    t = int(s[3:6], 2)
    s = s[6:]
    
    ret = []
    l = 0
    if (t == 4):
        num = parseFour(s)
        ret.append(int(num, 2))
        return ret, 6 + len(num) + len(num)//4
    else:
        i = s[0]
        s = s[1:]
        if (i == '0'):
            ret, l = parseIZero(s)
        elif (i == '1'):
            ret, l = parseIOne(s)
        
        val = None
        if (t == 0):
            val = sum(ret)
        elif (t == 1):
            val = prod(ret)
        elif (t == 2):
            val = min(ret)
        elif (t == 3):
            val = max(ret)
        elif (t == 5):
            val = 1 if ret[0] > ret[1] else 0
        elif (t == 6):
            val = 1 if ret[0] < ret[1] else 0
        elif (t == 7):
            val = 1 if ret[0] == ret[1] else 0
        
        return [val], l + 7
        
        

with open('data.txt') as file:
    hexData = file.read()
    binData = ''.join([format(int(x, 16), "0>4b") for x in hexData])
    
    num = parse(binData)
    print(num)
            