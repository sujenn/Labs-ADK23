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

with open("../rawindex.txt", "r", encoding = "latin-1") as f:
    byteCounter = -1
    byteStart = 0
    #word = ""
    #newWord = ""
    #en while loop som kör genom hela I
    letter = f.read(1)
    f.seek(0)
    f.seek(1607306748)
    while(letter != ""):
        print(letter)
        newWord = ""
        letter = f.read(1)
        byteCounter += 1
        while(letter.isalpha() and len(newWord) < 3):
            newWord += letter
            letter = f.read(1)
            byteCounter += 1
        if(len(newWord) == 1):
            newWord = newWord + "  "
        elif(len(newWord) == 2):
            newWord = newWord + " "
        
        #if(word != newWord):
            #behövs en extra check för att kolla om platsen är -1?
        indexForA = hash(newWord)
        if(aIndex[indexForA] == -1):
            aIndex[indexForA] = byteStart
            print(newWord, byteStart)
        #print(newWord, byteStart)
        #word = newWord
        #byteStart = byteCounter + 1
        #else: 
        nextLetter = f.read(1)
        byteCounter += 1
        while(nextLetter != "\n"):
            if(nextLetter == ""):
                letter = ""
            nextLetter = f.read(1)
            byteCounter += 1
        byteStart = byteCounter + 1
        
        '''nextLetter = f.read(1)
        byteCounter += 1
        while(nextLetter != "\n"):
            nextLetter = f.read(1)
            byteCounter += 1'''
print(aIndex)
