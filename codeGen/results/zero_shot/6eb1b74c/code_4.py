def min_steps(t, s_list):
    steps = 0
    used_strings = set()
    for i in range(len(t)):
        for s in s_list:
            if t[i:i+len(s)] == s and s not in used_strings:
                used_strings.add(s)
                steps += 1
    return steps
