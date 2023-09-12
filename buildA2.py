
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
        word = "  " + word
    elif(len(word) == 2):
        word = " " + word
    return word


with open("../rawindex.txt", "r", encoding = "latin-1") as f:
    sameWord = False
    byteStart = 0
    line = f.readline()
    word = makeWord(line)

    while(True):
        if(word == ""):
            break
        if(sameWord == False):
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


with open("A.txt", "a") as A:
    for line in aIndex:
        A.write(str(line) + "\n")

        
