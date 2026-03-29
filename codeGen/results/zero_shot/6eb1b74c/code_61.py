def find_strings_to_use(t, trie):
    used_strings = []
    current_position = 0
    while current_position < len(t):
        found = False
        for i, s_i in enumerate(test_cases[1:]):
            if trie.search(s_i[current_position:current_position+len(s_i)]):
                found = True
                used_strings.append(i+1)
                break
        if not found:
            return -1
        current_position += len(s_i)
    return used_strings

for t in test_cases[0]:
    min_steps = find_min_steps(t, trie)
    print(min_steps)
    strings_to_use = find_strings_to_use(t, trie)
    for i, s_i in enumerate(strings_to_use):
        print(i+1, strings_to_use.index(s_i)+1)
