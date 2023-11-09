

V = int(input())
E = int(input())
m = int(input()) + 2
edges = []
singleNodes = [0] * V

for i in range(E):
    u, v = map(int, input().split())
    singleNodes[u - 1] = 1
    singleNodes[v - 1] = 1
    edges.append([u,v])

for i in range(V):
    if singleNodes[i] == 0:
        V += 1
        E += 1
        edges.append([i + 1, V])
        if m == 3:
            m += 1
V += 2
E += 1

print(V)
print(E)
print(m)
#Vilka skådisar som kan ta vilka roller 
allActorsExceptOneDiva = ''
for i in range(m - 2):
    allActorsExceptOneDiva += str(i + 2) + ' '
for i in range(V - 2):
    print(str(m - 2) + ' ' + allActorsExceptOneDiva)
print('2 1 ' + str(m))
print('2 1 ' + str(m))

#Vilka roller som ingår i vilka scener
for i in range(E - 1):
    print(str(2) + ' ' + str(edges[i][0]) + ' ' + str(edges[i][1]))
print(str(2) + ' ' + str(V-1) + ' ' + str(V))
