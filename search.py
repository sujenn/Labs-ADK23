import math

def hashHelper(number):
    # a-z becomes 1-26
    if(number > 96 and number < 123):
        return number - 96
    # å and ä becomes 27 resp. 28
    elif(number == 228 or number == 229):
        return number - 201
    # ö becomes 29
    elif(number == 246):
        return number - 217
    # space and all other characters become 0
    else:
        return 0

def hash(word):
    word += '   '
    first = hashHelper(ord(word[0].lower()))
    second = hashHelper(ord(word[1].lower()))
    third = hashHelper(ord(word[2].lower()))

    return((first*900)+(second*30)+third)

aIndex = []
with open("A.txt", "r", encoding = "latin-1") as A:
    while (True):
        nextVar = A.readline()
        if(nextVar == ""):
            break
        aIndex.append(nextVar)

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
        lower = int(posI)
        higher = int(posINext)
        
        while (higher > lower):
            mid = math.floor((lower + higher) / 2)
            I.seek(mid)
            I.readline
            lineList = I.readline().split()
            if(lineList[0] < userInput):
                lower = mid - 1
            elif(lineList[0] > userInput):
                higher = mid + 1
            else:
                higher = mid 
                
        I.seek(lower)
        lineList = []
        while(True):
            lineWord = I.readline().split()
            if(lineWord[0] == userInput):
                #with open("../korpus", "r", encoding = "latin-1") as L:
                #return lineList[1]
                lineList.append(lineWord)
            if(lineWord[0] > userInput):
                #return "Not found"
                return lineList

print(searchAlg()[0])