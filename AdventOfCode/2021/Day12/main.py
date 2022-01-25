import re
from collections import deque

def is_upper(string):
    for c in string:
        if not c.isupper():
            return False
    return True

def is_twice(tab, val):
    count = 0
    for x in tab:
        if x == val:
            count += 1
    
    if count == 2:
        return True
    return False

def BFS(start, end, graph, double_visit):
    path = (start,)
    q = deque()
    q.append(path)
    ret = set()
    dv = double_visit
    while len(q):
        temp = q.popleft()
        last_node = temp[-1]
        if last_node == end:
            ret.add(temp)
        for link in graph[last_node]:
            if (link == dv) and (not is_twice(temp, dv)):
                new_path = temp + (link,)
                q.append(new_path)
            elif is_upper(link) or (link not in temp):
                new_path = temp + (link,)
                q.append(new_path)
    return ret
        

graph = {}

with open('file.txt') as file:
    for line in file.readlines():
        out = re.split('([a-zA-Z]+[a-zA-Z])', line)
        graph.setdefault(out[1], [])
        graph[out[1]].append(out[3])
        graph.setdefault(out[3], [])
        graph[out[3]].append(out[1])


qi = BFS('start', 'end', graph, 'qi')
jt = BFS('start', 'end', graph, 'jt')
br = BFS('start', 'end', graph, 'br')
wb = BFS('start', 'end', graph, 'wb')
aa = BFS('start', 'end', graph, 'aa')
br = BFS('start', 'end', graph, 'br')
hf = BFS('start', 'end', graph, 'hf')
    
print(len(qi.union(jt, br, wb, aa, br, hf)))