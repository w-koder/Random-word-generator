import random
import numpy
import functools
import rule_generator
MAX_CHANGE_COUNT = 500





def sort_by_length(in_str):
    return -len(in_str)


def generate(grammarToGenerate):
    orderedGrammar = list(grammarToGenerate.keys())
    orderedGrammar = sorted(orderedGrammar, key=sort_by_length)
    convergesCount = 0
    obj = rule_generator.andrew_rule_generator()
    # we always start with first nonterminal, with the first entry of dictionary
    word = 'expression'
    changeCount = 0
    end = False
    while not end:
        changed = False
        for key in orderedGrammar:
            res = word.find(key)
            if res != -1:
                changed = True
                changeCount += 1
                word = word.replace(key, obj.generate(key, grammarToGenerate, changeCount))
                # if changeCount > 2:
                #     word = word.replace(key, rule_generator(key, grammarToGenerate), 1)
                # else:
                #     word = word.replace(key, easy_chose_rule_from_grammar(key, grammarToGenerate), 1)
                if changeCount >= MAX_CHANGE_COUNT:
                    end = True  # only for break
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
        return word
    else:
        return None
