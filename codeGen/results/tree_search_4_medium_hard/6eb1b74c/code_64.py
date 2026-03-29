from collections import defaultdict

def min_steps_to_color_text(text, strings):
    n = len(strings)
    dp = {(i, frozenset({})): float('inf') for i in range(len(text) + 1)}
    dp[(0, frozenset(range(n)))] = 0
    
    for i in range(1, len(text) + 1):
        for unused_strings in list(dp.keys()):
            if i <= unused_strings[0] and not any(s in text[i-1:i+len(s)] for s in strings):
                dp[(i, unused_strings[1])] = dp[(i-1, unused_strings[1])]
            else:
                min_steps = float('inf')
                for j, string in enumerate(strings):
                    if i + len(string) <= len(text) and text[i:i+len(string)] == string:
                        min_steps = min(min_steps, dp.get((i+len(string), unused_strings - {j}), float('inf')) + 1)
                dp[(i, set(unused_strings[1] for unused_string in unused_strings[1]))] = min_steps
    
    return dp.get((len(text), frozenset({})), -1)

# Read input
q = int(input())
for _ in range(q):
    t = input().strip()
    n = int(input())
    strings = [input().strip() for _ in range(n)]
    
    # Solve the problem
    min_steps, usage = min_steps_to_color_text(t, strings)
    
    if min_steps == -1:
        print(-1)
    else:
        print(min_steps)
        for i in range(1, min_steps + 1):
            pos, unused_strings = next(((pos, unused_strings) for pos, unused_strings in dp.keys() if dp[(pos, unused_strings)] == i), None)
            string_index = next((j for j, s in enumerate(strings) if s in t[pos-1:pos+len(s)]), None)
            print(f"{string_index} {pos}")
