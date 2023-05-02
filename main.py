from itertools import permutations
 
def generateWord(letters):
    return permutations(letters)
 
words = generateWord(['f', 'i'])
# Print the obtained permutations
for i in list(words):
    print (i)