from itertools import permutations
 
def generateWord(letters, n):
    return permutations(letters, n)
 
words_3_letters = generateWord(['o', 'b', 'b', 'a', 's'], 3)
words_4_letters = generateWord(['o', 'b', 'b', 'a', 's'], 4)
words_5_letters = generateWord(['o', 'b', 'b', 'a', 's'], 5)

def isWordCorrect(word):
    f = open('./words/' + word[0] +'_words.txt', encoding="utf8")
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

def checkAllWords(letters_3, letters_4, letters_5):
    correctWords = []
    for word in letters_3:
        str = ' '
        str = str.join(word)
        str = str.replace(' ','')
        if isWordCorrect(str):
            correctWords.append(str)
    for word in letters_4:
        str = ' '
        str = str.join(word)
        str = str.replace(' ','')
        if isWordCorrect(str):
            correctWords.append(str)
    for word in letters_5:
        str = ' '
        str = str.join(word)
        str = str.replace(' ','')
        if isWordCorrect(str):
            correctWords.append(str)
    return correctWords

print(checkAllWords(words_3_letters, words_4_letters, words_5_letters))
