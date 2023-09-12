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
    if(len(word) == 1):
        word = "  " + word
    elif(len(word) == 2):
        word = " " + word
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
            I.readline()
            lineList = I.readline().split()
            if(lineList[0] < userInput):
                lower = mid + 1
            elif(lineList[0] > userInput):
                higher = mid - 1
            else:
                higher = mid
                
        I.seek(lower)
        lineList = []
        while(True):
            lineWord = I.readline()
            if(lineWord == "\n"):
                return lineList
            lineWord = lineWord.split()
            if(lineWord[0] == userInput):
                lineList.append(lineWord)
            if(lineWord[0] > userInput):
                if(len(lineList) == 0):
                    return -1
                else:
                    with open("../korpus", "r", encoding = "latin-1") as L:
                        L.seek(int(lineList[0][1]) - 30)    #Få det att funka på första o sista test case också
                        answerLine = ""
                        ansChar = L.read(1)
                        charCount = 0
                        while(charCount < 60 + len(lineList[0][0])): 
                            if(ansChar != "\n"):
                                answerLine += ansChar
                            else:
                                answerLine += " "
                            ansChar = L.read(1)
                            charCount += 1
                        return answerLine
                        #return(L.read(60))
                #return lineList

answer = searchAlg()
if(answer == -1):
    print("Not found")
else:
    print(answer)

#Vid sökning av siffror blir det error. ValueError: negative seek position -1