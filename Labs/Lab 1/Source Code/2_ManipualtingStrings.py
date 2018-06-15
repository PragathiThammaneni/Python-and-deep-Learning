# 2.  Python function that accepts a sentence of words from user and display thefollowing:
# a. Middle word.
# Longest word in the sentence.
# Reverse all the words in sentence

sentence = input("Enter the sentence: ") # input taken from the user
words_list = sentence.split()
longest = 0
for word in words_list:
    if len(word) > longest:
        longest = len(word)
        longest_word = word # finding the longest word in the sentence
print("The longest word is %s" % longest_word)
word_reversed = sentence[::-1] # finding the reversed string from all the words in the  given sentence
print("Sentence of reversed words : %s " % word_reversed)
no_of_words = len(words_list)
middle_word = []
if no_of_words%2==0: # finding the middle word in the given sentence
    middle_word.append(words_list[(no_of_words//2)-1])
    middle_word.append(words_list[no_of_words//2])
else:
    middle_word.append(words_list[no_of_words//2])
print("Middle word is : %s" % middle_word)