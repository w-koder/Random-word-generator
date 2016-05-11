import random
import re

signs = re.compile("\+ | \* | \?")
REG = "-?[0-9]*5+68" # [0 - 9]
o = ""

def fill(RE, i, o):
    while i < RE.__len__():
        if re.match("\(", RE[i]):
            j = i + 1
            while RE[j] != ')':
                j += 1
            str = RE[i+1:j]
            if re.match(signs, RE[j+1]) is None:
                fill(str, 0)
            else:
                if RE[j+1] == '?':
                    N = random.randint(0, 1)
                elif RE[j+1] == '*':
                    N = random.randint(0, 10)
                else:
                    N = random.randint(1, 10)
                for k in range(N):
                    fill(str, 0)
        elif re.match("\[", RE[i]):
            if re.match(signs, RE[i+5]) is None:
                X = random.randint(int(RE[i + 1]), int(RE[i + 3]))
                o += X
                i += 5
            else:
                if RE[i+5] == '?':
                    N = random.randint(0, 1)
                elif RE[i+5] == '*':
                    N = random.randint(0, 10)
                else:
                    N = random.randint(1, 10)
                for k in range(N):
                    X = random.randint(int(RE[i + 1]), int(RE[i + 3]))
                    o += X
                i += 6
        else:
            if re.match(signs, RE[i+1]) is None:
                o += RE[i]
                i += 1
            else:
                if RE[i+1] == '?':
                    N = random.randint(0, 1)
                elif RE[i+1] == '*':
                    N = random.randint(0, 10)
                else:
                    N = random.randint(1, 10)
                for k in range(N):
                    o += RE[i]
                i += 2
fill(REG, 0, o)
print(o)
