
nbrOfRoles = int(input())
nbrOfScenes = int(input())
nbrOfActors = int(input())

rolesActors = []
scenesRoles = []

roleCounter = [0] * nbrOfActors # The index is the actor and a number of roles the actor can have at that index #KOLLA OM LÄNGD ÄR RÄTT
actorRoleAnswer = [[] for _ in range(nbrOfRoles * 2 + 1)]  
allAssingedRoles = []

scenesRoles.append([1, 3])

'''
#build max scenes
for i in range(4000):
    stringScene = ''
    for j in range(1, 600):
        stringScene += str(j + 1) + ' '
    eRow = list(map(int, stringScene.split()))
    scenesRoles.append(eRow)

for i in range(600):
    sb = ''
    for j in range(400):
        sb += str(j + 1) + ' '
    vRow = list(map(int, sb.split()))
    rolesActors.append(vRow)
'''
for _ in range(nbrOfRoles):
    vRow = list(map(int, input().split()))
    vRow.pop(0)
    rolesActors.append(vRow)


for _ in range(nbrOfScenes):
    eRow = list(map(int, input().split()))
    eRow.pop(0)
    scenesRoles.append(eRow)

# For finding the actor that can play the most roles
for i in range(len(rolesActors)):
    for j in range(len(rolesActors[i])):
        roleCounter[rolesActors[i][j] - 1] += 1
roleCounter.pop(0)  # We do not need to include diva 1 and 2
roleCounter.pop(0)

# find roles for the divas
diva1Count = 0
found = False
invalidRolesDivas = set() # behöver nog inte lägga in de i början
for i in range(nbrOfRoles):
    if 1 in rolesActors[i]:
        for j in range(nbrOfScenes):
            if (i + 1) in scenesRoles[j]:
                invalidRolesDivas.update(scenesRoles[j])
        #print(invalidRolesDivas)
        for l in range(nbrOfRoles):
            if not((l + 1) in invalidRolesDivas) and (2 in rolesActors[l]):
                actorRoleAnswer[1] = [l + 1]
                allAssingedRoles.append(l + 1)
                actorRoleAnswer[0] = [i + 1]
                allAssingedRoles.append(i + 1)
                found = True
                break
        '''if len(allAssingedRoles) == 0:
            invalidRolesDivas.clear()'''
        if found:
            break

# Find more roles for diva 1 and 2
for i in range(nbrOfScenes):
    if actorRoleAnswer[0][0] in scenesRoles[i] or actorRoleAnswer[1][0] in scenesRoles[i]:
        invalidRolesDivas.update(scenesRoles[i])

for diva in range(1, 3):
    for i in range(nbrOfRoles):
        if not((i + 1) in invalidRolesDivas) and (diva in rolesActors[i]):
            actorRoleAnswer[diva - 1].append(i + 1)
            allAssingedRoles.append(i + 1)
            for j in range(nbrOfScenes):
                if (i + 1) in scenesRoles[j]:
                    invalidRolesDivas.update(scenesRoles[j])

# OBS MÅSTE ADDERA 3 TILL CURRENTBESTACTOR! EN FÖR NOLL-INDEX, 2 FÖR VI HAR TAGIT BORT DIVA 1 OCH 2
# Find role for actor

currentBestActor = -1
invalidRolesActor = set([actorRoleAnswer[0][0], actorRoleAnswer[1][0]])
for i in range(len(roleCounter)):
    foundActor = False
    currentBestActor = roleCounter.index(max(roleCounter))
    roleCounter[currentBestActor] = 0
    currentBestActor += 3   # OBS HAR GJORT CURRENTBESTACTOR 1-INDEX...
    # Look for if there is a role that the actor can have
    for rowRolesActors in range(len(rolesActors)):
        if (currentBestActor in rolesActors[rowRolesActors]) and not((rowRolesActors + 1) in allAssingedRoles):
            actorRoleAnswer[currentBestActor - 1].append(rowRolesActors + 1)
            allAssingedRoles.append(rowRolesActors + 1)
            invalidRolesActor.update([rowRolesActors + 1])   #KAN VARA FEL
            foundActor = True
            break
    # Look for more roles for currentBestActor
    if foundActor:
        # Look for all invalid roles from sceneRoles
        for i in range(nbrOfScenes):
            if actorRoleAnswer[currentBestActor - 1][0] in scenesRoles[i]:
                invalidRolesActor.update(scenesRoles[i])
 
        # Look for all roles 
        for i in range(nbrOfRoles):
            if not((i + 1) in invalidRolesActor) and (currentBestActor in rolesActors[i]) and not((i + 1) in allAssingedRoles):
                actorRoleAnswer[currentBestActor - 1].append(i + 1)
                allAssingedRoles.append(i + 1)
                for j in range(nbrOfScenes):
                    if (i + 1) in scenesRoles[j]:
                        invalidRolesActor.update(scenesRoles[j])
# Add super actors
rolesNotAssigned = []
for i in range(nbrOfRoles):
    if not((i + 1) in allAssingedRoles):
        rolesNotAssigned.append(i + 1)

for i in range(len(rolesNotAssigned)):
    actorRoleAnswer[nbrOfActors + i].append(rolesNotAssigned[i])

# Print
countActors = 0
for i in range(len(actorRoleAnswer)):
    if len(actorRoleAnswer[i]) > 0:
        countActors += 1
print(countActors)        

for i in range(len(actorRoleAnswer)):
    if len(actorRoleAnswer[i]) > 0:
        answerString = str(i + 1) + ' ' + str(len(actorRoleAnswer[i])) + ' '
        for j in range(len(actorRoleAnswer[i])):
            answerString += str(actorRoleAnswer[i][j]) + ' '
        print(answerString)
