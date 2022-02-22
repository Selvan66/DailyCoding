from queue import PriorityQueue

class Graph:
    def __init__(self, num):
        self.v = num
        self.edges = {}
        self.visited = []
        
    def add_edge(self, u, v, weight):
        self.edges.setdefault(u, [])
        self.edges[u].append((v, weight))

def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)
        print(current_vertex)
        for neighbor in graph.edges[current_vertex]:
            distance = neighbor[1]
            if neighbor[0] not in graph.visited:
                old_cost = D[neighbor[0]]
                new_cost = D[current_vertex] + distance
                if new_cost < old_cost:
                    pq.put((new_cost, neighbor[0]))
                    D[neighbor[0]] = new_cost
    return D




c = []
with open('file.txt') as file:
    for line in file.readlines():
        a = [int(x) for x in list(line.rstrip())]
        b = []
        for i in range(5):
            b.extend([x + i if x + i <= 9 else x + i - 9 for x in a])           
        c.append(b)
tab = []

for i in range(5):
    for t in c:
        tab.append([x + i if x + i <= 9 else x + i - 9 for x in t])
        

width = 100 * 5
height = 100 * 5
g = Graph(width * height)
for i in range(width):
    for j in range(height):
        print((i, j))
        if i + 1 < width:
            g.add_edge((width * j) + i, (width * j) + i + 1, tab[j][i + 1])
        if i - 1 >= 0:
            g.add_edge((width * j) + i, (width * j) + i - 1, tab[j][i - 1])
        if j + 1 < height:
            g.add_edge((width * j) + i, (width * (j + 1)) + i, tab[j + 1][i])
        if j - 1 >= 0:
            g.add_edge((width * j) + i, (width * (j - 1)) + i, tab[j - 1][i])

print(dijkstra(g, 0)[249999])