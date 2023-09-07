
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

def makeWord(byteIndex):
    word = ""
    letter = f.read(1)  
    byteC = byteIndex + 1         
    while(letter.isalpha() and len(word) < 3):
        word += letter
        letter = f.read(1)
        byteC += 1
    if(len(word) == 1):
        word = word + "  "
    elif(len(word) == 2):
        word = word +  " "
    return [word, byteC, byteIndex]

with open("../rawindex.txt", "r", encoding = "latin-1") as f:
    sameword = False
    byteCounter = 0
    byteIndex = 0
    word, byteCounter, byteIndex = makeWord(byteIndex)
    f.seek(byteCounter)

    while(f.read(1) != ""):
        byteCounter += 1
        if(sameword == False):
           indexPos = hash(word)
        if(aIndex[indexPos] == -1):
            aIndex[indexPos] = byteIndex
            print(word + " " + str(aIndex[indexPos]))
        nextLetter = f.read(1)
        byteCounter += 1
        while(nextLetter != "\n"):
            nextLetter = f.read(1)
            byteCounter += 1

        newWord, byteCounter, byteIndex = makeWord(byteCounter)

        if(word == newWord):
            sameWord = True
        else:
            word = newWord
            sameWord = False