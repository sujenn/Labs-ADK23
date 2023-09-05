with open("../korpus", "r", encoding = "latin-1") as f:
    with open("../I.txt", "a", encoding = "latin-1") as I:
        byteCounter = 0
        byteStart = 0
        while True:
            oneChar = f.read(1)
            if(oneChar.isalpha() == False):
                word = ""
                for i in range(byteStart, byteCounter):
                    f.seek(i)
                    word += f.read(1)
                f.seek(byteCounter + 1)
                I.write(word + " " + str(byteStart) + "\n")
                nextChar = f.read(1)
                if(nextChar.isalpha() == False):
                    byteStart = byteCounter + 2
                    byteCounter += 1
                else:
                    byteStart = byteCounter + 1
                    f.seek(byteCounter + 1)
            elif(oneChar == ""):
                break
            byteCounter += 1
            if(byteCounter == 100):
                break
    

