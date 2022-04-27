
vers = []

def parse(s):
    if ((not len(s)) or ('1' not in s)):
        return

    v = int(s[0:3], 2)
    vers.append(v)
    t = int(s[3:6], 2)
    s = s[6:]
    
    if (t == 4):
        i = s[0]
        s = s[1:]
        while (i != '0'):
            s = s[4:]
            if (not len(s)):
                break
            i = s[0]
            s = s[1:]
        parse(s[4:])
    else:
        i = s[0]
        s = s[1:]
        if (i == '0'):
            l = int(s[0:15], 2)
            parse(s[15:(l + 15)])
            parse(s[(l + 15):])
        else:
            parse(s[11:])

with open('data.txt') as file:
    hexData = file.read()
    binData = ''.join([format(int(x, 16), "0>4b") for x in hexData])
    
    parse(binData)
    print(sum(vers))
            