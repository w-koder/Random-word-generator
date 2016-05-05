# Bad news:
# It still needs a lot of optimization (fortunately I know how to manage that)
# Now it works only for arithmetical expressions
# Part with braces (first if) isn't finished yet, that part requires some recursion

import random
import re

RE = "-?[0 - 9][a-z][0-9]"
signs = re.compile("\+ | \* | \?")
o = "" # o for object, it's our return
i = 0
while i < RE.__len__():
    if re.match("\(", RE[i]):
        j = i + 1
        while RE[j] != ')':
            j += 1
    elif re.match("\[", RE[i]):
        X = random.randint(RE[i+1], RE[i+3])
        if re.match(signs, RE[i+5]) is None:
            o += X
        else:
            if RE[i+5] == '?':
                N = random.randint(0, 1)
            elif RE[i+5] == '*':
                N = random.randint(0, 10)
            else:
                N = random.randint(1, 10)
            for k in range(N):
                o += X
    else:
        if re.match(signs, RE[i+1]) is None:
            o += RE[i]
        else:
            if RE[i+1] == '?':
                N = random.randint(0, 1)
            elif RE[i+1] == '*':
                N = random.randint(0, 10)
            else:
                N = random.randint(1, 10)
            for k in range(N):
                o += RE[i]
