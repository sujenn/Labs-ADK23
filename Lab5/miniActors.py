
V = int(input())
E = int(input())
m = int(input())
roleList = []
edgesList = []
checkEdges = [-1] * V

# Read what actors can be which roles
for _ in range(V):
    actors = []
    for _ in range(int(input())):
        actors.append(int(input()))
    roleList.append(actors)

# Read what roles can be in which scens
for _ in range(E):
    u, v = map(int, input().split())
    edgesList.append([u,v])

for i in range(E):
    checkEdges[edgesList[i][0] - 1] = edgesList[i][1]
    checkEdges[edgesList[i][1] - 1] = edgesList[i][0]

for i in range(len(checkEdges)):
    if len(checkEdges[i]) < V - 1:
        break