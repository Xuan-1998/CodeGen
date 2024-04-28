from sys import stdin

def solve():
    n = int(stdin.readline())
    s = stdin.readline().strip()
    
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(2**n):
        wins = 0
        for j in range(n-1, -1, -1):
            if (i & (1 << j)) > 0:
                if s[j] == 'W':
                    wins += 1
                else:
                    break
        dp[n-1][wins] += 1
    
    for j in range(n-2, -1, -1):
        for i in range(n+1):
            if (i & (1 << j)) > 0:
                if s[j] == 'W':
                    dp[j][i] = dp[j][i-1]
                else:
                    dp[j][i] += dp[j+1][i-1]
    
    winning_teams = []
    for i in range(n+1):
        if dp[0][i] > 0:
            winning_teams.append(i)
    
    print(' '.join(map(str, sorted(winning_teams))))

if __name__ == '__main__':
    solve()
