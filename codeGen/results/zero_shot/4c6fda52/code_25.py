import sys

def min_changes(n, k, s):
    seen = set()
    changes = 0
    for i in range(len(s) - k + 1):
        window = s[i:i+k]
        if window not in seen:
            changes += 1
            seen.add(window)
    return changes

while True:
    n, k = map(int, input().split())
    s = input()
    print(min_changes(n, k, s))
