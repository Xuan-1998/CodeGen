import sys

n, m, h = map(int, input().split())
players = list(map(int, input().split()))

players.sort(reverse=True)

ways = 0
total_ways = 1
for i in range(m):
    if i == h:
        total_ways *= (players[i] + n - 1) // n
    else:
        ways += players[h]
        total_ways *= players[i]

if total_ways > 0:
    print(ways / total_ways)
else:
    print(-1.0)
