
def hashHelper(number):
    if(number == 32):
        return 0
    elif(number < 123):
        return number - 96
    elif(number < 230):
        return number - 201
    else:
        return number - 217

def hash(word):
    word += '   '
    first = hashHelper(ord(word[0].lower()))
    second = hashHelper(ord(word[1].lower()))
    third = hashHelper(ord(word[2].lower()))

    return((first*900)+(second*30)+third)

aIndex = [-1]*27000

def makeWord(line):
    word = ""
    i = 0
    if(line == ""):
        return ""
    while(line[i].isalpha() and i < 3):
        word += line[i]
        i += 1
    if(len(word) == 1):
        word = word + "  "
    elif(len(word) == 2):
        word = word +  " "
    return word


with open("../rawindex.txt", "r", encoding = "latin-1") as f:
    sameword = False
    byteStart = 0
    line = f.readline()
    
    while(True):
        word = makeWord(line)
        if(word == ""):
            break
        if(sameword == False):
            indexPos = hash(word)
            if(aIndex[indexPos] == -1):
                aIndex[indexPos] = byteStart
        byteStart += len(line) 
        line = f.readline()
        newWord = makeWord(line)
        if(word == newWord):
            sameWord = True
        else:
            word = newWord
            sameWord = False

def searchAlg():
    userInput = input().lower()
    posA = hash(userInput)
    posI = aIndex[posA]
    posINext = aIndex[posA + 1]

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
                with open("../korpus", "r", encoding = "latin-1") as L:
                    return lineList[1]
            if(lineList[0] > userInput):
                return "Not found"