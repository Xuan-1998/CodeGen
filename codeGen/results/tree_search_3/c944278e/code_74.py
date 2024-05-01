n = int(input())
s = input()

dp = [[0]*(2**i) for i in range(n+1)]
for i in range(1, n+1):
    for j in range(2**i):
        if s[i-1] == '0':
            dp[i][j] = 0
        else:
            wins = sum((k & (2**(i-1))) > 0 for k in range(j))
            dp[i][j] = wins + dp[i-1][wins]

print(*[i for i in range(2**n) if s.count('1') <= i], sep='\n')
