from pprint import pprint
#for a given sentance we'll have to find the most repeated charecter
hello = "This is a common Interview Question"
sentance = hello.lower() #for lower charecters
char_frequency = {}
for char in sentance:
    if char in char_frequency:
        char_frequency[char] += 1
    else: 
        char_frequency[char] = 1

#pprint(char_frequency, width= 1) 1 way

pprint(sorted(char_frequency.items()))