

#test = open("../korpus", "r", encoding = "latin-1")
#print(test.read())
#test.close()

with open("../korpus", "r", encoding = "latin-1") as f:
    print(f.read(20))

