import math

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö']

def hashHelper(number):
    # a-z becomes 1-26
    if(number > 96 and number < 123):
        return number - 96
    # å and ä becomes 27 resp. 28
    elif(number >= 228 and number <= 230):
        return number - 201
    # ö and ø becomes 29
    elif(number == 246 or number == 248):
        return 29
    # space and all other characters become 0
    elif(number >= 224 and number <= 227):
        return 1
    elif(number == 223):
        return 19
    elif(number == 231):
        return 3
    elif(number >= 232 and number <= 235):
        return 5
    elif(number >= 236 and number <= 239):
        return 9
    elif(number == 240):
        return 4
    elif(number == 241):
        return 14
    elif(number >= 242 and number <= 245):
        return 15
    elif(number >= 249 and number <= 252):
        return 21
    elif(number == 253 or number == 255):
        return 25
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

def findAmount(lower, userInput):
    count = 0
    with open("../rawindex.txt", "r", encoding = "latin-1") as I:
        I.seek(lower)
        lineWord = I.readline().split()
        if(lineWord[0] < userInput):
            lineWord = I.readline().split()
        while(lineWord[0] == userInput):
            lineWord = I.readline().split()
            count += 1
            if(len(lineWord) == 0):
                break  
    return count

def searchAlg(userInput):
    posA = hash(userInput)
    posI = aIndex[posA]
    if(posA == 26999):
        posINext = aIndex[posA]
    else:
        i = 1
        while (int(aIndex[posA + i]) == -1):
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
            else:
                higher = mid
    return lower


def findOccurrences(lower, userInput):
    with open("../rawindex.txt", "r", encoding = "latin-1") as I:
        count = 0
        I.seek(lower)      
        isFirstRun = True
        lineList = []
        while(count < 25):
            lineWord = I.readline()
            #ska kanske ta bort
            if(lineWord == "\n"):       
                return lineList
            if(lineWord == ""):       
                return lineList
            lineWord = lineWord.split()
            if(lineWord[0] == userInput):
                lineList.append(lineWord)
                count += 1
            else: 
                if(isFirstRun == True):
                    isFirstRun = False
                    continue
                else:
                    break
            isFirstRun = False
        return lineList

def printk(lineList):
    if(len(lineList) == 0):
        return -1
    else:
        with open("../korpus", "r", encoding = "latin-1") as L:
            allOccurrences = []
            for i in range(len(lineList)):
                readLen = 30 + int(lineList[i][1])
                answerLine = ""
                if (int(lineList[i][1]) < 30):
                    for _ in range(30 - int(lineList[i][1])):
                        answerLine += " "
                    L.seek(0)
                else:
                    L.seek(int(lineList[i][1]) - 30)    #Få det att funka på första o sista test case också
                    readLen = 60
                ansChar = L.read(1)
                charCount = 0
                while(charCount < readLen + len(lineList[i][0])): 
                    if(ansChar != "\n"):
                        answerLine += ansChar
                    else:
                        answerLine += " "
                    ansChar = L.read(1)
                    charCount += 1
                allOccurrences.append(answerLine)
            return allOccurrences

print("Write your search word: ")
userInput = input().lower()
validWord = False
while(validWord == False):
    validChar = True
    for letter in userInput:
        if(letter not in alphabet):
            validChar = False
    if(validChar == True):
        validWord = True
    else:
        print("Your word is not valid, try again!")
        userInput = input().lower()  

lower = searchAlg(userInput)
amount = findAmount(lower, userInput)
list25 = findOccurrences(lower, userInput)
answer = printk(list25)
if(answer == -1):
    print("Not found")
else:
    print("Det finns " + str(amount) + " förekomster av ordet.") 
    if(len(answer) < 25):
        for i in range(len(answer)):
            print(answer[i])
    else:
        for i in range(25):
            print(answer[i])
        print("Det finns fler förekomster att visa, vill du se dem? Yes/No")
        userI = input().lower()
        if(userI == "yes"):
            with open("../rawindex.txt", "r", encoding = "latin-1") as I:
                I.seek(lower)     
                I.readline()
                lineList = []
                while(True):
                    lineWord = I.readline()
                    if(lineWord == "\n"):   
                        break
                    lineWord = lineWord.split()
                    if(lineWord[0] == userInput):
                        lineList.append(lineWord)
                    else: 
                        break
                answer = printk(lineList)
                for i in range(25, len(lineList)):
                    print(answer[i])

#Vid sökning av siffror blir det error. ValueError: negative seek position -1