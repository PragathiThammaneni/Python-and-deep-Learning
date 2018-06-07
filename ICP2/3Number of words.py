fname = "feed.txt"
import sys

f = open(fname, "r")
# Open file for input
lines=0
mostWordsInLine = 0
for lineOfText in f.readlines():
    lines += 1
    wordCount = 0
    print(str(lineOfText))
    f1=lineOfText.split()
    wordCount=wordCount+len(f1)
    if len(f1) > mostWordsInLine:
        mostWordsInLine = len(f1)
    print ("Word count:" +str(wordCount))