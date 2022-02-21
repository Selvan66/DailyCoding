
template = ''
with open('file1.txt') as file:
    template = file.readline()

end_letter = template[-1]
pattern = {}
with open('file2.txt') as file:
    for line in file.readlines():
        par = line.rstrip().split(' -> ')
        pattern[par[0]] = par[0][0] + par[1] + par[0][1]

# Spliting text to 3 letters grups
q = {}
for i in range(len(template) - 1):
    gen = pattern[template[i:i+2]]
    q.setdefault(gen, 0)
    q[gen] += 1

steps = 40

for i in range(steps - 1):
    items = list(q.items());
    for (key, value) in items:
        gen1 = pattern[key[0:2]]
        gen2 = pattern[key[1:3]]
        q.setdefault(gen1, 0)
        q.setdefault(gen2, 0)
        q[gen1] += value
        q[gen2] += value
        q[key] -= value

# Counting letters
counter = {}
for (key, value) in q.items():
    counter.setdefault(key[0], 0)
    counter.setdefault(key[1], 0)
    counter[key[0]] += value
    counter[key[1]] += value
counter[end_letter] += 1
values = sorted(counter.values())
print(values[-1] - values[0])
    