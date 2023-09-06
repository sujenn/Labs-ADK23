def hashHelper(number):
    #tänker att vi kanske kan lägga till "   " efter alla ord som inputas 
    #klarar då av ord som t.ex i, ö, är
    if(number == 32):
        return 29
    elif(number < 123):
        return number - 97
    elif(number < 230):
        return number - 202
    else:
        return number - 218

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

AIndex = [-1]*27000
print(AIndex)

with open("../rawindex.txt", "r", encoding = "latin-1") as f:
    for i in range (30):
        for j in range (30):
            for k in range (30):
                f.read(1)
                AIndex[(i*900)+(j*30)+k] = f.readline
        