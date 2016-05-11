# Returns tuple (rules_dictionary, tokens_dictionary)
def text_to_dict(file):
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

    # Splitting inputed text to rules and spreading rules across dictionaries
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

    return rules_dict, tokens_dict
