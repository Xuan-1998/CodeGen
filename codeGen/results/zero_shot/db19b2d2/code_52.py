def probability(n, m, h, s):
    total_players = sum(s)
    
    if total_players < n:
        return -1
    
    players_from_h = s[h-1]
    probability = 0.0
    
    for i in range(m):
        if i == h-1:
            probability += (s[i] / total_players) * players_from_h
        else:
            probability += (s[i] / total_players)
    
    return 1 - (1 - probability) ** n

n, m, h = map(int, input().split())
s = list(map(int, input().split()))

print(format(probability(n, m, h, s), ".6f"))
