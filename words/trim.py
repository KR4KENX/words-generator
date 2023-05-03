def createOnLetterFiles(firstLetter):
    # create new file
    f = open(firstLetter+'_words.txt', 'x', encoding='utf8')
    # open dictionary
    dict = open('../odm.txt', encoding='utf8')
    # loop over dictionary
    while True:
        line = dict.readline()
        # is line not blank
        if line != '':
            line = line.lower()
            # is line starts on our letter
            if line[0] == firstLetter:
                f.write(line)
        else:
            break


createOnLetterFiles('z')