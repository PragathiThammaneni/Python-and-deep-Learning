#Python program to get the sentence from the user and then count the frequency of each word in it using dictionary. The words as keys should be in sorted manner in dictionary.

sentence = input("Enter the data for word count: ").split() # Taking the user input
ls = []
for i in sentence: # iterating to find the count of each word from the provided input

    word_count = sentence.count(i)  # Python count function, count()
    ls.append((i,word_count))


mydict = dict(ls) # appending the word and word count to a dictionary

print("Output:",mydict) # printing the formed output

print("Sorted Output:",dict(sorted(mydict.items())))# printing the sorted output