import random

WORD_COUNT = 500
MAX_CHANGE_COUNT = 1000


def chose_rule_from_grammar(nonterminal, grammarToChose) -> str:
    size = len(grammarToChose[nonterminal])
    chose = random.randint(0, size - 1)
    return grammarToChose[nonterminal][chose]


def generate(grammarToGenerate):
    convergesCount = 0
    for j in range(WORD_COUNT):
        word = "E"  # we always start with first nonterminal, with the first entry of dictionary
        changeCount = 0
        while changeCount < MAX_CHANGE_COUNT:
            changed = False
            for key in grammarToGenerate.keys():
                res = word.find(key)
                if res != -1:
                    changed = True
                    changeCount += 1
                    word = word.replace(key, chose_rule_from_grammar(key, grammarToGenerate), 1)
            if not changed:
                break
        if changeCount >= MAX_CHANGE_COUNT:
            print("false")
        else:
            print("true")
            convergesCount += 1
        print(word)
    print("Converges Count = " + str(convergesCount) + " out of " + str(WORD_COUNT))
    print("Converges Probability = " + str(convergesCount / WORD_COUNT))

# palindrome grammar
# grammar = {"S": ["E", "a", "b", "aSa", "bSb"]}

# easy arithmetic grammar
# grammar = {"S": ["S+S", "S-S"]}
# for i in range(2):
#     grammar["S"].append(i.__str__())

# harder arithmetic grammar
grammar = {"E": ["E+S", "E-S", "S"],
           "S": ["S*F", "S/F", "F"],
           "F": ["(E)"]}    # and any number
for i in range(10):
    grammar["F"].append(i.__str__())

generate(grammar)
