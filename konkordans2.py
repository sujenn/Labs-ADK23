from hash import hash 
import math
import sys
import time

#st = time.time()
# Read from A.txt and save to aIndex
aIndex = []
with open("A.txt", "r", encoding = "latin-1") as A:
    while (True):
        nextVar = A.readline()
        if(nextVar == ""):
            break
        aIndex.append(nextVar)

# Find the number of occurrences. To improve search speed we only read the number 
# of occurrences to count them, but dont save them.
def findAmount(lower, userInput):
    count = 0
    with open("../rawindex.txt", "r", encoding = "latin-1") as I:
        I.seek(lower)
        lineWord = I.readline().split()
        while(lineWord[0] == userInput):
            lineWord = I.readline().split()
            count += 1
            if(len(lineWord) == 0):
                break  
    return count

# Binary search to find the first appearance in rawindex of the input word or the index before.
# It may return the index before because lower is not guaranteed to be a byte poistion 
# at the start of a new line in rawindex.
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
        
        while (higher - lower > 1000):
            mid = math.floor((lower + higher) / 2)
            I.seek(mid)
            I.readline()
            lineList = I.readline().split()
            if(lineList[0] < userInput):
                lower = mid + 1
            else:
                higher = mid
        I.seek(lower)
        #I.seek(posA)    #for linear search
        while True:
            x = I.tell()
            lineList = I.readline().split()
            if lineList[0] == userInput:
                #found
                return x
            if lineList[0] > userInput:
                #not found
                return x

# Read 30 chars before and after the searched word for every occurrnace and prints it. When 25 words 
# are printed and there are more words left, promts user and asks if they want to see the rest.
def addChars(lineList):
    with open("../korpus", "r", encoding = "latin-1") as L:
        for i in range(len(lineList)):
            readLen = 30 + int(lineList[i][1])
            answerLine = ""
            if (int(lineList[i][1]) < 30):
                for _ in range(30 - int(lineList[i][1])):
                    answerLine += " "
                L.seek(0)
            else:
                L.seek(int(lineList[i][1]) - 30)    
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
            print(answerLine)

# read from args and keyboard input. Checks if any extra args exists and then that it is valid (Swedish Alphabet)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö']
if(len(sys.argv) > 1):
    userInput = sys.argv[1].lower()
else: 
    print("Your word is not valid, try again: ")
    userInput = input().lower()
    if(userInput == ""):
        sys.exit()
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
        if(userInput == ""):
            sys.exit() 

# Linear search from first occurrence of the searched word in constant memory complexity, 
# calls addChars to print each word (with chars before and after) and keep track of 25 
def printWords(lower, amount):
    with open("../rawindex.txt", "r", encoding = "latin-1") as I:
        I.seek(lower)  
        count = 0
        while(True):
            if(count == 25 and amount > 25):
                #et = time.time()
                print("Det finns fler förekomster att visa, vill du se dem? Yes/No")
                userI = input().lower()
                if(userI != "yes"):
                    break
            lineWord = I.readline()
            if(lineWord == ""):   
                break
            lineWord = lineWord.split()
            if(lineWord[0] == userInput):
                addChars([lineWord])
                count += 1
            else:
                break
    #return et

# Run the functions
lower = searchAlg(userInput)
amount = findAmount(lower, userInput)

# Check if the word was found, if there are more than 25 occurrances, 
# they can be printed but this may take more than 1 sec
if(amount == 0):
    print("Not found")
else:
    print("Det finns " + str(amount) + " förekomster av ordet.") 
    #et = printWords(lower, amount)
    printWords(lower, amount)

'''elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')'''

    

