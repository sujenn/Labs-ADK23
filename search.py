def searchAlg():
    print("Write your search word: ")
    userInput = input().lower()
    posA = hash(userInput)
    posI = aIndex[posA]
    i = 1
    while (aIndex[posA + i] == -1):
        i += 1
    posINext = aIndex[posA + i]

    with open("../rawindex.txt", "r", encoding = "latin-1") as I:
        lower = posI
        higher = posINext
        while (higher - lower > 1000):
            mid = (lower + higher) / 2
            I.seek(mid)
            lineList = I.readline().split()
            if(lineList[0] <= userInput):
                lower = mid
            else:
                higher = mid
        I.seek(lower)
        while(True):
            lineList = I.readline().split()
            if(lineList[0] == userInput):
                #with open("../korpus", "r", encoding = "latin-1") as L:
                return lineList[1]
            if(lineList[0] > userInput):
                return "Not found"

print(searchAlg())