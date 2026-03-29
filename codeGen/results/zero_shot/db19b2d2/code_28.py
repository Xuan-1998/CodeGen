n, m, h = map(int, input().split())
s = list(map(int, input().split()))
total_players = sum(s)

if total_players < n:
    print(-1)
else:
    prob = s[h-1] / total_players
    print(prob)
