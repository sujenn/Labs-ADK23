
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
    with open("A.txt", "a" , encoding = "latin-1") as A:
        sameword = False
        byteStart = 0
        line = f.readline()
        oldHash = 0

        while(True):
            word = makeWord(line)
            if(word == ""):
                break
            if(sameword == False):
                newHash = hash(word)
                decrement = newHash
                if(oldHash + 1 != newHash):
                    while(decrement + 1 > oldHash):
                        A.write('{:010}'.format(byteStart))
                        decrement -= 1
                else:
                    A.write('{:010}'.format(byteStart))
                oldHash = newHash
                
            byteStart += len(line)      #Kolla om /n är inräknat
            line = f.readline()
            newWord = makeWord(line)
            if(word == newWord):
                sameWord = True
            else:
                word = newWord
                sameWord = False
#print(aIndex)



        
