#Take an Input file. Use the simple approach below to summarize a text file:a. Read the fileb. Apply lemmatization on the wordsc. Apply the bigram on the textd. Calculate the word frequency (bi-gram frequency) of the words (bi-grams)f. Choose top five bi-grams that have been repeated mostg. Go through the original text that you had in the fileh. Find all the sentences with those most repeated bi-gramsi. Extract those sentences and concatenatej. Enjoy the summarization

#imported the nltk modules , to find out lemmatization,bigram,bigram-frequency,extracting the sentences and concatination
import nltk
from nltk.util import bigrams
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
#loaded the  input file -input,txt
input_data=open('input.txt',"r")
#reading  the data from the input file
data=input_data.read()
#get each word from sentence - Tokenization
words=word_tokenize(data)
#apply lemmitizer - Lemmitization
lemm=WordNetLemmatizer()
list=[]
list1=[]
print("Lemmitizor:"+"\n")
#printing the lemmitizer  for each word
for k in words:
    print("Lemmatizor for word "+k+" is "+lemm.lemmatize(k))

print("\n")
print("Bigrams:"+"\n")
#printing the  bigram from the data loaded -from the text file
for x in bigrams(words):
    print(x)
    list.append(x)
print("\n")
#appending each word in bigram to a list to calculate the  frequencies
for y in list:
    for z in y:
        list1.append(z)
#calculating the  bigram word frequency and top 5 repeated words
count=Counter(list1)
count_most=count.most_common(5)
most=[i[0] for i in count_most]
#printing the  bigram word frequency and the top 5 repeated words
print("\n Bigram word frequencies\n")
print(count)
print("\nTop 5 repeated words\n")
print(count_most)
#calculating the  Senteces with repeated bigrams
cat=""
repeated_sent=sent_tokenize(data)
print("\n Senteces with repeated bigrams:\n ")
for m in repeated_sent:
    if any(word in m for word in most):
        print(m)
        cat=cat+m
#printing the  Senteces with repeated bigrams
print("\n Sentence after concatenation is: \n"+cat)