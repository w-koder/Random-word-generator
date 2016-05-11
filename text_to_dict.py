#Returns tuple (rules_dictionary, tokens_dictionary)
def text_to_dict(file,  rough_splitting_by_bars = False):
    rules_dict = {}
    tokens_dict = {}
    grammar_text = ""

    skip_trigger = False
    multiline_skip_trigger = False
    screened_trigger = False
    braces_trigger = False

    for file_line in file:
        file_line = file_line.replace(' operator ', ' ')
        for char_index in range(len(file_line)):

            if (file_line[char_index] == '\''
                and not skip_trigger
                and not multiline_skip_trigger
                and not braces_trigger):
                screened_trigger ^= True

            if (screened_trigger == False):
                if file_line[char_index] == '#':
                    skip_trigger = True
                if file_line[char_index] == '\n':
                    skip_trigger = False

                if file_line[char_index] == '{':
                    braces_trigger = True
                if file_line[char_index] == '}':
                    braces_trigger = False

                if file_line[char_index:char_index+2] == "/*":
                    multiline_skip_trigger = True
                if file_line[char_index-2:char_index] == "*/":
                    multiline_skip_trigger = False

            if (file_line[char_index] != ' '
                and file_line[char_index] != '\n'
                and file_line[char_index] != '\t'
                and file_line[char_index] != '\r'
                and not skip_trigger
                and not multiline_skip_trigger
                and not braces_trigger):
                grammar_text += file_line[char_index];

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

    if (rough_splitting_by_bars):

        #implementig sort of service string to be able to split rules by |
        def service_string_implementation (dict):
            for key, rule in dict.items():
                quotes_count = 0
                service_string_places = []

                for i in range(len(rule)):
                    if rule[i] == '\'':
                        quotes_count += 1
                    if rule[i] == "|" and quotes_count%2 == 1:
                        service_string_places.append(i)
                        quotes_count = 1

                if len(service_string_places) > 0:
                    new_rule = rule[:service_string_places[0]]
                    for i in range(len(service_string_places)):
                        new_rule += "%SERVICE_STRING%"
                        if i < len(service_string_places)-1:
                            new_rule += rule[service_string_places[i] + 1:service_string_places[i + 1]]
                        else :
                            new_rule += rule[service_string_places[i] + 1:]
                    rules_dict[key] = new_rule

        service_string_implementation(rules_dict)
        service_string_implementation(tokens_dict)

        for key, rule in rules_dict.items():
            new_rules = []
            for subrule in rule.split("|"):
                new_rules.append (subrule.replace("%SERVICE_STRING%", "|"))
            rules_dict[key] = new_rules

        for key, rule in tokens_dict.items():
            new_rules = rule.split("|")
            for subrule in new_rules:
                new_rules.append(subrule.replace("%SERVICE_STRING%", "|"))
            tokens_dict[key] = new_rules


    return (rules_dict, tokens_dict)
