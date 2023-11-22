
V = int(input())
E = int(input())
m = int(input())
roleList = []
edgesList = []
checkEdges = [-1] * V
actorsRoles = [-1] * 3  # Kanske måste ändra
invalidNodes = []


# Read what actors can be which roles
for _ in range(V):
    a = map(int, input().split())
    actors = []
    for i in a:
        actors.append(a[i + 1])
    roleList.append(actors)

# Read what roles can be in which scens
for _ in range(E):
    n, u, v = map(int, input().split())
    edgesList.append([u,v])

for i in range(E):
    checkEdges[edgesList[i][0] - 1] = edgesList[i][1]
    checkEdges[edgesList[i][1] - 1] = edgesList[i][0]

# Find which roles the divas can have
diva1 = True
for i in range(len(checkEdges)):
    if len(checkEdges[i]) < V - 1:
        if diva1:
            actorsRoles[0] = [1, i + 1]
            diva1 = False
        else: 
            actorsRoles[1] = [2, i + 1]
            break

od = [1, 0]
for i in range(2): 
    potenialNodes = []
    for node in edgesList:
        if node[0] == actorsRoles[i][1] or node[1] == actorsRoles[i][1]:
            invalidNodes.append(node[0])
            invalidNodes.append(node[1])
        if node[0] == actorsRoles[od[i]][1] or node[1] == actorsRoles[od[i]][1]:
            invalidNodes.append(node[0])
            invalidNodes.append(node[1])
        if (node[0] != actorsRoles[i][1] and node[0] != actorsRoles[od[i]][1]) or (node[1] != actorsRoles[i][1] and node[1] != actorsRoles[od[i]][1]):
            potenialNodes.append([node[0], node[1]])

    for node in potenialNodes:
        if not(node[0] in invalidNodes):
            if node[0] in roleList[0]:
                actorsRoles[0].append(node[0])
                invalidNodes.append(node[1])
        if not(node[1] in invalidNodes):
            if node[1] in roleList[0]:
                actorsRoles[0].append(node[1])
                invalidNodes.append(node[0])

print(actorsRoles)