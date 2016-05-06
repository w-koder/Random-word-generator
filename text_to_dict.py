#Returns tuple (rules_dictionary, tokens_dictionary)
def text_to_dict(file ):

    rules_dict = {}
    tokens_dict = {}
    grammar_text = ""
    skip_trigger = False

    for file_line in file:
        file_line = file_line.replace(' operator ', ' ')
        for char in file_line:
            if char == '\n':
                skip_trigger = False

            if char == '#':
                skip_trigger = True

            if(char != ' '
                and char != '\n'
                and char != '\t'
                and char != '\r'
                and skip_trigger == False):
                grammar_text += char;

    #Splitting inputed text to rules and spreading rules across dictionaries
    for line in grammar_text.split(';'):
        if line != '':
            if (line.startswith("grammar")
                or line.startswith("//")):
                continue
            rule = line.split(':', 1)
            if rule[0][0] == rule[0][0].capitalize():
                tokens_dict[rule[0]] = rule[1]
            else:
                rules_dict[rule[0]] = rule[1]

    #implementig sort of KOSTYL to be able to split rules by |
    #Do not look at it if you want to be mentally health
    #Please, do not
    def kostyl_implementation (dict):
        for key, rule in dict.items():
            quotes_count = 0
            kostyl_places =[]

            for i in range(len(rule)):
                if rule[i] == '\'':
                    quotes_count += 1
                if rule[i] == "|" and quotes_count%2 == 1:
                    kostyl_places.append(i)
                    quotes_count = 1

            if len(kostyl_places) > 0:
                new_rule = rule[:kostyl_places[0]]
                for i in range(len(kostyl_places)):
                    new_rule += "T.H.E.K.O.S.T.Y.L"
                    if i < len(kostyl_places)-1:
                        new_rule += rule[kostyl_places[i] + 1:kostyl_places[i + 1]]
                    else :
                        new_rule += rule[kostyl_places[i] + 1:]
                    #I've warned you: do not look
                rules_dict[key] = new_rule

    kostyl_implementation(rules_dict)
    kostyl_implementation(tokens_dict)

    for key, rule in rules_dict.items():
        new_rules = []
        for subrule in rule.split("|"):
            new_rules.append (subrule.replace("T.H.E.K.O.S.T.Y.L", "|"))
        rules_dict[key] = new_rules

    for key, rule in tokens_dict.items():
        new_rules = rule.split("|")
        for subrule in new_rules:
            new_rules.append(subrule.replace("T.H.E.K.O.S.T.Y.L", "|"))
        tokens_dict[key] = new_rules

    return (rules_dict, tokens_dict)
