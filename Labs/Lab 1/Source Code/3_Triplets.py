# Python program to find triplets in the list which gives the sum of zero.
import json
str_list = input("Enter in a list: ")
my_list = json.loads(str_list)
s = sorted(my_list)
zeroset = set()
for k in range(len(s)):
    target = -s[k]
    i, j = k + 1, len(s) - 1
    while i < j:
        sum_two = s[i] + s[j]
        if sum_two < target:
            i += 1
        elif sum_two > target:
            j -= 1
        else:
            zeroset.add((s[k], s[i], s[j]))
            i += 1
            j -= 1
print(zeroset) # printing the zero set that formed