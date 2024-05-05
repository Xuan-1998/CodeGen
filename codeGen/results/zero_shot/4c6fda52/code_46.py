import sys

def min_changes(s, k):
    changes = 0
    for c in set(s[:k-1]):
        if c not in s[:k-1]:
            changes += 1
    return changes

t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    print(min_changes(s, k))
