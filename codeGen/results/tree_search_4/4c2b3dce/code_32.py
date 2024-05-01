import sys

def has_abba(s):
    state = 0
    indices = []
    for i, c in enumerate(s):
        if c == 'A':
            state -= 1
        elif c == 'B':
            state += 1
        if state == 0:
            indices.append(i)
    return len(indices) >= 2

s = input()
print("YES" if has_abba(s) else "NO")
