import sys
n, m, h = map(int, sys.stdin.readline().split())
players = []
for _ in range(m):
    s = list(map(int, sys.stdin.readline().split()))
    for i, si in enumerate(s):
        players.append((i+1, si))
players.sort()

dept_players = {}
for player in players:
    dept, num_players = player
    if dept not in dept_players:
        dept_players[dept] = 0
    dept_players[dept] += num_players

prob = 0
for i in range(len(players)):
    if players[i][0] != h:
        prob += (1 - players[i][1]/n)**(n-1)
prob /= (1 - 1/n)**n

if sum(dept_players.values()) < n:
    print(-1)
else:
    print(prob)
