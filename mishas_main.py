import text_to_dict
import random
import main
import regex
file = open("Corundum.g4", "r")
rules, tokens = text_to_dict.text_to_dict(file, True)
length = 5
print(tokens)
for index in range(length):
    var = main.generate(rules)
    for key in tokens.keys():
        index = 0
        l1 = len(tokens[key])
        print(l1)
        if l1 > 1:
            index = random.randint(0, l1-1)
        print(key)
        print(tokens[key][index])
        genReg = regex.fill(tokens[key][index], 0, '')
        genReg += ' '

        var = var.replace(str(key), genReg)
        file = open('files\\' + str(index) + '.rb', 'w')
        file.write(var[1:len(var)-1])


