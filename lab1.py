


with open("../korpus", "r", encoding = "latin-1") as f:
    #print(f.read(5000))
    with open("../I.txt", "a", encoding = "latin-1") as I:
        byteCounter = 0
        byteStart = 1
        while True:
            oneChar = f.read(1)
            byteCounter += 1
            if(oneChar == " " or oneChar == "\\n" or oneChar == "." or oneChar == "," or oneChar == ","):
                word = ""
                for i in range(byteStart, byteCounter):
                    f.seek(i)
                    word += f.read(1)
                I.write(word + " " + str(byteStart) + "\n")
                byteStart = byteCounter 
            elif(oneChar == ""):
                break
            if(byteCounter == 100):
                break
        
    
    
    '''with open("../I.txt", "a+", encoding = "latin-1") as I:
        I.write("hej2")
        print(I.read())  '''      
    


