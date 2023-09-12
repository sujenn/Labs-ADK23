with open("../rawindex.txt", "r", encoding = "latin-1") as f:
    f.seek(19070516)
    print(f.readline())
    #print(f.read(50))