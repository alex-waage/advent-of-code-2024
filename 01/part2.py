f = open("01/input.txt", "r")
l = []
r = []
total = 0

for i in f:
    l.append(i[0:5])
    r.append(i[8:13])

l.sort()
r.sort()

for x in l:
    c = int(x) * r.count(x)
    total += c
    
print(total)