#Program to  the number of vowels in a string -
#Input is taken and compared with the set of vowels by iterating over the input string

userstring = input("Enter a string: ") #Taking the user input
count = 0  # set the variable as count and intialize with zero
vowels = set("aeiou") # created a set of vowels
for letter in userstring: # iterated over each letter and counting the vowels from the string
    if letter in vowels:
        count += 1
print ("Vowel  count:",count) # print statement to output the vowel count