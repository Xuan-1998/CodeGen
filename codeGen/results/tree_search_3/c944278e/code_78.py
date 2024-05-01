def find_winning_teams(n, s):
    dp = [[False] * (1 << n) for _ in range(n)]
    
    for i in range(n):
        prev_winner = 0
        for j in range(1 << n):
            if not dp[i][j]:
                continue
            if s[i] == '1':
                dp[i+1][j | prev_winner] = True
            prev_winner = j
    
    winning_teams = [i for i in range(1 << n) if dp[-1][i]]
    
    return [bin(t, n)[2:].zfill(n) for t in winning_teams]

# Example usage:
n = 3
s = input().strip()
winning_teams = find_winning_teams(int(n), s)
print(*winning_teams, sep='\n')
