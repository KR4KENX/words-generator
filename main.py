from itertools import permutations
 
def generateWord(letters):
    return permutations(letters)
 
words = generateWord(['f', 'i'])

f = open('odm.txt', encoding="utf8")

def isWordCorrect(word):
    while True:
        line = f.readline()
        if line != '':
            line = line.replace(' ', '')
            line = line.replace('\n', '')
            line = line.split(',')
            if word in line:
                return True
        else:
            return False
        
print(isWordCorrect('zez'))