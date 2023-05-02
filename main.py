from itertools import permutations
 
def generateWord(letters):
    return permutations(letters)
 
words = generateWord(['l', 'o', 'a', 'd', 'r'])

def isWordCorrect(word):
    f = open('odm.txt', encoding="utf8")
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
        
for word in words:
    str = ' '
    str = str.join(word)
    str = str.replace(' ','')
    if isWordCorrect(str):
        print(str)