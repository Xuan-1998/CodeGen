import sys

n, m, h = map(int, input().split())
players_from_h = sum(1 for i in range(m) if i == h)
total_players = n + sum(i for i in range(m))
if total_players < n:
    print(-1)
else:
    prob = players_from_h / total_players
    print(prob)
