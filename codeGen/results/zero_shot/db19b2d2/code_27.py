n, m, h = map(int, input().split())
s = list(map(int, input().split()))

total_players = sum(s)

teams = total_players // n
if total_players % n > 0:  
    teams -= 1

probability = 1 - (s[h-1] / total_players) ** teams
if probability < 0:
    probability = -1

print(probability)
