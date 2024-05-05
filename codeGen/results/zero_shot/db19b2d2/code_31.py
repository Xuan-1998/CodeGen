import sys
from math import comb

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
h = int(sys.stdin.readline().strip())

s = list(map(int, sys.stdin.readline().split()))

total_players = sum(s)

if total_players < n:
    print(-1)
else:
    prob = 0
    for i in range(h):
        prob += s[i] * comb(total_players - sum(s[:i]) - sum(s[i+1:]), n-1, exact=True) / (total_players ** n)
    print(prob)
