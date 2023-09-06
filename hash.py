
def hashHelper(number):
    #tänker att vi kanske kan lägga till "   " efter alla ord som inputas 
    #klarar då av ord som t.ex i, ö, är
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

'''
print("Please enter a word:")
userInput = input()
print(hash(userInput)) '''

aIndex = [-1]*27000

byteCounter = 0
def makeWord():
    letter = f.read(1)  
    byteCounter += 1          
    while(letter.isalpha() and len(word) < 3):
        word += letter
        letter = f.read(1)
        byteCounter += 1
    if(len(word) == 1):
        word = "  " + word
    elif(len(word) == 2):
        word = " " + word
    return word

with open("../rawindex.txt", "r", encoding = "latin-1") as f:
    word = makeWord()
    for i in range (30):
        for j in range (30):
            for k in range (30):
                sameWord = False
                while(sameWord or hash(word) == i*900 + j*30 + k):
                    if(aIndex[(i*900)+(j*30)+k] == -1):
                        aIndex[(i*900)+(j*30)+k] = byteCounter
                    nextLetter = f.read(1)
                    while(nextLetter != "\\"):
                        nextLetter = f.read(1)
                        byteCounter += 1
                    f.read(1)
                    byteCounter += 2
                    newWord = makeWord()
                    if(word != newWord):
                        word = newWord
                        sameWord = False
                    else:
                        sameWord = True

print("Här kommer den första: " + str(aIndex[0]))
print("Här kommer den andra: " + str(aIndex[1]))


        