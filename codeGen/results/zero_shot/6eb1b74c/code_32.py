import sys

def color_text(text, strings):
    used_strings = set()
    steps = 0

    for i in range(len(text)):
        found = False
        for s in strings:
            if text[i:i+len(s)] == s and s not in used_strings:
                used_strings.add(s)
                steps += 1
                break

    return steps, [(i, j) for (i, s), j in enumerate(used_strings)]

# Read input from stdin
t = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
strings = [sys.stdin.readline().strip() for _ in range(n)]

# Calculate the minimum number of steps needed
steps, used_strings = color_text(t, strings)

if steps == -1:
    print(-1)
else:
    print(steps)
    for i, s in enumerate(used_strings):
        print(i+1, s)
