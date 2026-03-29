import sys

def min_changes(s, k):
    changes = 0
    for i in range(k-1):
        if s[i] != 'R' and s[i] != 'G':
            changes += 1
    for i in range(k-1, len(s)):
        if s[i] != (s[(i-k+1)%len(s)]):
            changes += 1
    return changes

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    print(min_changes(s, k))
