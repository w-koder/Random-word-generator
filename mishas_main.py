import text_to_dict
import random
import main
import regex
file = open('Corundum.g4', 'r')
rules, tokens = text_to_dict.text_to_dict(file, True)
length = 20
print(tokens)
for progNum in range(length):
    random.seed(progNum)
    word = main.generate(rules)
    if word is not None:
        print(word)
        for key in tokens.keys():
            index = 0
            l1 = len(tokens[key])
            index = random.randint(0, l1-1)
            while True:
                genReg = regex.fill(tokens[key][index], 0, '')
                genReg += ' '
                newWord = word.replace(str(key), genReg, 1)
                if word != newWord:
                    word = newWord
                else:
                    break;

        out_file = open(str(progNum) + '.rb', 'w')      # 'files\\' +
        out_file.write(word)


