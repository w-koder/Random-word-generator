import random
import numpy
class rule_generator:
    def __init__(self):
        pass
    def generate(self, nonterminal, grammar, count)->str:
        pass

class andrew_simple_rule_generator(rule_generator):
    # if you try to set this function the converges become worse, but variety become better!
    # uniform distribution
    def generate(self, nonterminal, grammar, count) -> str:
        size = len(grammar[nonterminal])
        chose = random.randint(0, size - 1)
        return grammar[nonterminal][chose]


class andrew_rule_generator(rule_generator):
    # distribution by nonterminal number
    def generate(self, nonterminal, grammar, count):
        if count > 2:

            values = []
            sum = 0
            for ruleContent in grammar[nonterminal]:
                nonterminalCount = 0
                for key in grammar.keys():
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
            return numpy.random.choice(grammar[nonterminal], 1, False, probabilities)[0]

        else:
            a = andrew_simple_rule_generator()
            return a.generate(nonterminal, grammar, count)