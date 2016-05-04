import random
import numpy

WORD_COUNT = 2000
MAX_CHANGE_COUNT = 500


# if you try to set this function the converges become worse, but variety become better!
# uniform distribution
def easy_chose_rule_from_grammar(nonterminal, grammarToChose) -> str:
    size = len(grammarToChose[nonterminal])
    chose = random.randint(0, size - 1)
    return grammarToChose[nonterminal][chose]


# distribution by nonterminal number
def chose_rule_from_grammar(nonterminal, grammarToChose) -> str:
    values = []
    sum = 0
    for ruleContent in grammarToChose[nonterminal]:
        nonterminalCount = 0
        for key in grammarToChose.keys():
            res = ruleContent.find(key)
            if res != -1:
                nonterminalCount += 1
        if nonterminalCount == 0:
            nonterminalCount += 0.5
        values.append(nonterminalCount)
        sum += nonterminalCount

    probabilities = []
    for i in range(len(values)):
        values[i] = 1 / values[i]
    znam = 0
    for el in values:
        znam += el
    const = 1 / znam
    for i in range(len(values)):
        probabilities.append(const * values[i])
    return numpy.random.choice(grammarToChose[nonterminal], 1, False, probabilities)[0]


def generate(grammarToGenerate):
    convergesCount = 0
    for j in range(WORD_COUNT):
        word = "S"  # we always start with first nonterminal, with the first entry of dictionary
        changeCount = 0
        while changeCount <= MAX_CHANGE_COUNT:
            changed = False
            for key in grammarToGenerate.keys():
                res = word.find(key)
                if res != -1:
                    changed = True
                    changeCount += 1
                    word = word.replace(key, chose_rule_from_grammar(key, grammarToGenerate), 1)
                    if changeCount >= MAX_CHANGE_COUNT:
                        changed = False  # only for break
                        break
            if not changed:
                break
        # determine the consistence of nonterminals:
        converges = True
        for key in grammarToGenerate.keys():
            res = word.find(key)
            if res != -1:  # key in word
                converges = False
                break

        if converges:
            print("true")
            convergesCount += 1
        else:
            print("false")
        print(word)
    print("Converges Count = " + str(convergesCount) + " out of " + str(WORD_COUNT))
    print("Converges Probability = " + str(convergesCount / WORD_COUNT))


# palindrome grammar
# grammar = {"S": ["", "a", "b", "aSa", "bSb"]}

# easy arithmetic grammar
# grammar = {"S": ["S+S", "S-S"]}
# for i in range(2):
#     grammar["S"].append(i.__str__())

# harder arithmetic grammar
grammar = {"S": ["S+sum", "S-sum", "sum"],
           "sum": ["sum*F", "sum/F", "F"],  # not the best names for nonterminals
           "F": ["(S)"]}  # and any number
for i in range(10):
    grammar["F"].append(i.__str__())

generate(grammar)
