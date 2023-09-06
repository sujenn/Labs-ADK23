
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

def makeWord(byteC):
    word = ""
    letter = f.read(1)  
    byteC += 1          
    while(letter.isalpha() and len(word) < 3):
        word += letter
        letter = f.read(1)
        byteC += 1
    if(len(word) == 1):
        word = "  " + word
    elif(len(word) == 2):
        word = " " + word
    return [word, byteC]

with open("../rawindex.txt", "r", encoding = "latin-1") as f:
    byteCounter = 0
    word, byteCounter = makeWord(byteCounter)
    for i in range (30):
        for j in range (30):
            for k in range (30):
                sameWord = False
                while(sameWord or hash(word) == i*900 + j*30 + k):
                    if(aIndex[(i*900)+(j*30)+k] == -1):
                        aIndex[(i*900)+(j*30)+k] = byteCounter
                        print(str(word) + " " + str(byteCounter))
                    nextLetter = f.read(1)
                    while(nextLetter != "\\"):
                        nextLetter = f.read(1)
                        byteCounter += 1
                    f.read(1)
                    byteCounter += 2
                    newWord, byteCounter = makeWord(byteCounter)
                    if(word != newWord):
                        word = newWord
                        sameWord = False
                    else:
                        sameWord = True

print("Här kommer den första: " + str(aIndex[0]))
print("Här kommer den andra: " + str(aIndex[1]))


        