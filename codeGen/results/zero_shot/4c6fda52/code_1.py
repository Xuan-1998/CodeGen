import sys

def min_changes(s, k):
    n = len(s)
    changes = 0
    for i in range(k-1):
        if s[i] != (s[i+1] + s[i]).[-1]:
            changes += 1
    return changes

n, k = map(int, sys.stdin.readline().split())
s = list(sys.stdin.readline().strip())

print(min_changes(s, k))
