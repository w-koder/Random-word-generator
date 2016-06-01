# The main idea is to parse given regular expressions into units which can be directly put into token
# For that we should 'programm' all specific symbols, which can be met in our regular expression, such as *, + and so on
# Have a fun

import string
import random
import re

REG = "[a-zA-Z_][a-zA-Z0-9_]*'?'"                           # regular expression (further 're')
object = ""                                                 # this will be the result of this programm
id_first_symbol = string.ascii_letters + '_'                # this string contains all latin symbols and symbol '_'
id_else = string.ascii_letters + '_' + string.digits        # same + all digits. These two are for [a-zA-Z_] re
maxN = 10                                                   # that's max of possible symbol amount repeated by *, + or ?

def fill(RE, i, object):
    while i < RE.__len__():                                 # i - index of current symbol in REG
        if re.match("\(", RE[i]):
            j = i + 1
            while RE[j] != ')':                             # j - the end of the content of braces
                j += 1
            substring = RE[i+1:j]                           # so we withdraw that content
            if j+1 < RE.__len__():
                if re.match('\?', RE[j+1]):                 # this little switch will be met several times here
                    amount = random.randint(0, 1)           # someday I'll carry it out as independent function
                elif re.match('\*', RE[j+1]):               # but not today
                    amount = random.randint(0, maxN)        # it analyzes how many times the content should be repeated
                elif re.match('\+', RE[j+1]):
                    amount = random.randint(1, maxN)
                else:
                    amount = 1
                for k in range(amount):                     # so, we repeat it random amount of times, smaller than maxN
                    fill(substring, 0, object)
            else:
                fill(substring, 0, object)
        elif re.match("\[", RE[i]):                         # Further it's pretty much the same: we analyze spec symbol
            if RE[i+4] == ']':                              # we got and treat it the way it should be. Step by step we
                if i+5 < RE.__len__():                      # fill our object to the look it matches given re
                    flag = 0
                    if re.match('\?', RE[i + 5]):
                        amount = random.randint(0, 1)
                    elif re.match('\*', RE[i + 5]):
                        amount = random.randint(0, maxN)
                    elif re.match('\+', RE[i + 5]):
                        amount = random.randint(1, maxN)
                    else:
                        flag = 1
                        amount = 1
                    for k in range(amount):
                        object += (random.randint(int(RE[i + 1]), int(RE[i + 3]))).__str__()
                        #print("branch ", object)
                    if flag == 0:
                        i += 6
                    else:
                        i += 5
                else:
                    object += (random.randint(int(RE[i + 1]), int(RE[i + 3]))).__str__()
                    #print("branch ", object)
                    i += 5
            else:
                object += random.choice(id_first_symbol)
                #print("first ", object)
                amount = random.randint(0, maxN)
                for k in range(amount):
                    object += random.choice(id_else)
                    #print("else ", object)
                j = i + 1
                while RE[j] != '*':
                    j += 1
                i = j + 1
        elif re.match("\'", RE[i]):
            j = i + 1
            while re.match("\'", RE[j]) is None:
                object += RE[j]
                #print("quote ", object)
                j += 1
            i = j + 1
        else:
            if i+1 < RE.__len__():
                flag = 0
                if re.match('\?', RE[i + 1]):
                    amount = random.randint(0, 1)
                elif re.match('\*', RE[i + 1]):
                    amount = random.randint(0, maxN)
                elif re.match('\+', RE[i + 1]):
                    amount = random.randint(1, maxN)
                else:
                    flag = 1
                    amount = 1
                for k in range(amount):
                    object += RE[i]
                    #print("single ", object)
                if flag == 0:
                    i += 2
                else:
                    i += 1
            else:
                object += RE[i]
                #print("single ", object)
                i += 1
    return object

print(fill(REG, 0, object))
