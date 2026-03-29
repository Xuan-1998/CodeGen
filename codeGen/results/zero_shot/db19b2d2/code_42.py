import math

n, m, h = map(int, input().split())
s = list(map(int, input().split()))

total_players = sum(s)
if total_players < n:
    print(-1)
else:
    prob_team = 1 if s[h-1] >= n else 0
    prob = prob_team * math.ceil(total_players / n)
    print(prob)
