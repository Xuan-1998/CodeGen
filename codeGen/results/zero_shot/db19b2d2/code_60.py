import sys
from math import comb

# Read input from stdin
n, m, h = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

total_players = sum(s)

players_from_h = s[h-1]

probability = 0
for i in range(1, players_from_h+1):
    probability += (total_players - i) / total_players * comb(players_from_h, i)

print(probability)
