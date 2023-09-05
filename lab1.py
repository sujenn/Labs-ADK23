


with open("../korpus", "r", encoding = "latin-1") as f:
    #print(f.read(5000))
    with open("../I.txt", "a", encoding = "latin-1") as I:
        byteCounter = 0
        byteStart = 0
        while True:
            oneChar = f.read(1)
            
            #if(oneChar == " " or oneChar == "\\" or oneChar == "." or oneChar == "," or oneChar == "-"):
            if(oneChar.isalpha() == False):
                word = ""
                for i in range(byteStart, byteCounter):
                    f.seek(i)
                    word += f.read(1)
                f.seek(byteCounter + 1)
                I.write(word + " " + str(byteStart) + "\n")
                byteStart = byteCounter + 1
            elif(oneChar == ""):
                break

            byteCounter += 1

            if(byteCounter == 100):
                break
        
    
    
    '''with open("../I.txt", "a+", encoding = "latin-1") as I:
        I.write("hej2")
        print(I.read())  '''      
    


