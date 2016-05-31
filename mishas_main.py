import random

import parser_rules
import regex
from files1 import text_to_dict

file = open('Corundum.g4', 'r')
rules, tokens = text_to_dict.text_to_dict(file, True)
length = 20
print(tokens)

for progNum in range(length):
    random.seed(progNum)
    #word = main.generate(rules)
    word = parser_rules.generate(rules)
    if word is not None:
     #   print(word)
        sorted_tokens = sorted(tokens.keys(), key=parser_rules.sort_by_length)
        for key in sorted_tokens:
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

        out_file = open('files1\\'+str(progNum) + '.rb', 'w')      # 'files\\' +
        out_file.write(word)
