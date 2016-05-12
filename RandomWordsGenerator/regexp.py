# It finally works!
# Though still only for numbers
# And there's one thing I don't get:
# Check-prints show that it works just fine
# But final print(object) returns empty string

"""
INT : [0-9]+; 
FLOAT : [0-9]*'.'[0-9]+; 
ID : [a-zA-Z_][a-zA-Z0-9_]*; 
ID_GLOBAL : '$'ID; 
ID_FUNCTION : ID'?';
"""

import string
import random
import re

REG = "[a-zA-Z_][a-zA-Z0-9_]*'?'"
object = ""
id_first_symbol = string.ascii_letters + '_'
id_else = string.ascii_letters + '_' + string.digits

def fill(RE, i, object):
    while i < RE.__len__():
        if re.match("\(", RE[i]):
            j = i + 1
            while RE[j] != ')':
                j += 1
            substring = RE[i+1:j]
            if j+1 < RE.__len__():
                if re.match('\?', RE[j+1]):
                    amount = random.randint(0, 1)
                elif re.match('\*', RE[j+1]):
                    amount = random.randint(0, 10)
                elif re.match('\+', RE[j+1]):
                    amount = random.randint(1, 10)
                else:
                    amount = 1
                for k in range(amount):
                    fill(substring, 0, object)
            else:
                fill(substring, 0, object)
        elif re.match("\[", RE[i]):
            if RE[i+4] == ']':
                if i+5 < RE.__len__():
                    flag = 0
                    if re.match('\?', RE[i + 5]):
                        amount = random.randint(0, 1)
                    elif re.match('\*', RE[i + 5]):
                        amount = random.randint(0, 10)
                    elif re.match('\+', RE[i + 5]):
                        amount = random.randint(1, 10)
                    else:
                        flag = 1
                        amount = 1
                    for k in range(amount):
                        object += (random.randint(int(RE[i + 1]), int(RE[i + 3]))).__str__()
                        print("branch ", object)
                    if flag == 0:
                        i += 6
                    else:
                        i += 5
                else:
                    object += (random.randint(int(RE[i + 1]), int(RE[i + 3]))).__str__()
                    print("branch ", object)
                    i += 5
            else:
                object += random.choice(id_first_symbol)
                print("first ", object)
                amount = random.randint(0, 10)
                for k in range(amount):
                    object += random.choice(id_else)
                    print("else ", object)
                j = i + 1
                while RE[j] != '*':
                    j += 1
                i = j + 1
        elif re.match("\'", RE[i]):
            object += RE[i+1]
            print("quote ", object)
            i += 3
        else:
            if i+1 < RE.__len__():
                flag = 0
                if re.match('\?', RE[i + 1]):
                    amount = random.randint(0, 1)
                elif re.match('\*', RE[i + 1]):
                    amount = random.randint(0, 10)
                elif re.match('\+', RE[i + 1]):
                    amount = random.randint(1, 10)
                else:
                    flag = 1
                    amount = 1
                for k in range(amount):
                    object += RE[i]
                    print("single ", object)
                if flag == 0:
                    i += 2
                else:
                    i += 1
            else:
                object += RE[i]
                print("single ", object)
                i += 1
fill(REG, 0, object)
