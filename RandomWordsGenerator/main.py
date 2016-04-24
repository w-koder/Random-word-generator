import random


def chose_rule_from_grammar(nonterminal, grammar) -> object:
    size = len(grammar[nonterminal])
    chose = random.randint(0, size - 1)
    return grammar[nonterminal][chose]


def generate(grammar):
    for j in range(1000):
        word = "S"
        for i in range(1000000):
            res = word.find("S")
            if res != -1:
                word = word.replace("S", chose_rule_from_grammar("S", grammar), 1)
            else:
                break
        print(word)


grammar = {"S": ["E", "a", "b", "aSa", "bSb"]}
#grammar = {"S": ["S+S", "S-S"]}
#for i in range(2):
#    grammar["S"].append(i.__str__())

generate(grammar)
