import sys

n, m, h = map(int, input().split())
s = list(map(int, input().split()))

total_players = sum(s)
players_from_h = s[h-1]

probability = players_from_h / total_players if total_players > n else -1

print(probability)
