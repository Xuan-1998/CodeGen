from collections import deque

def winning_teams(n, s):
    dp = [False] * (1 << n)
    winning_teams = set()
    
    for mask in range(1 << n):
        if not any((mask & (1 << i)) and ((s >> i) & 1) for i in range(n)):
            continue
        if all(((mask & (1 << i)) and ((s >> i) & 1)) or (~mask & (1 << i)) and ((~s >> i) & 1) for i in range(n)):
            dp[mask] = True
            winning_teams.add(mask)
    
    return [bin(i)[2:].zfill(n) for i in sorted(winning_teams)]

n = int(input())
s = bin(int(input(), 2))[2:].zfill(18)
print(*winning_teams(n, s), sep='\n')
