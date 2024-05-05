from collections import deque

def min_steps_to_color_text(text, string_set):
    dp = {(0, frozenset()): 0}
    for i in range(1, len(text) + 1):
        s_set = set()
        for j in range(len(string_set)):
            if text[i - len(string_set[j]):i] == string_set[j]:
                s_set.add(string_set[j])
                break
        dp[(i, frozenset(s_set))] = min((dp.get((i - 1, frozenset(d)), float('inf')) for d in [d | {s} for s in s_set]), default=float('inf'))
    return dp.get((len(text), frozenset()), -1)

used_strings = set()
for i in range(len(input().strip()) + 1):
    input_line = input().strip()
    if i == 1:
        text = input_line
    elif i <= len(input().splitlines()[0]):
        string_set = [line.strip() for line in input().splitlines()][1:]
        break
print(min_steps_to_color_text(text, set(string_set)))
