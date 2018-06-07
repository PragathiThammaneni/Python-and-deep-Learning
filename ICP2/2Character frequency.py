f = open("character", "r")

for i in f:
    l = len(i)
    file1 = open("output.txt","a")
    file1.write(i[:-1]+","+str(l-1)+'\n')
file1.close()