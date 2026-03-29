import sys

# Read input from stdin
n, m, h = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

total_players = sum(s)

players_from_h = s[h-1]

probability = (total_players - players_from_h) / total_players if total_players > 0 else -1

print(probability)
