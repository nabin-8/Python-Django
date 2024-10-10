from pprint import pprint
# Built in data structures in python

# 1.Lists
numbers=[1,2,3,4]

# Extercise
sentence="This is a common interview question"
char_frequency={}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
# pprint(char_frequency, width=1)

char_frequency_sorted=sorted(
    char_frequency.items(), 
    key=lambda kv:kv[1],
    reverse=True)
print(char_frequency_sorted[0])