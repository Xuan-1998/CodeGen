import sys

n, m, h = map(int, sys.stdin.readline().split())
players = list(map(int, sys.stdin.readline().split()))
total_players = sum(players)

if total_players < n:
    print(-1)
else:
    probability = (sum([player for i, player in enumerate(players) if i + 1 == h]) / total_players)
    print(probability)
