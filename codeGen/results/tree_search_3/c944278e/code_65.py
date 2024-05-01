import sys

def solve(n, s):
    dp = [[] for _ in range(n+1)]
    dp[0].append(0)
    
    for i in range(1, n+1):
        for j in range(2**i):
            if (s[i-1] >> (i-1) & 1) == 1:
                dp[i].extend([j]+team for team in dp[i-1][j] if s[i-1][team] == 'W')
            else:
                dp[i].extend(team for team in dp[i-1][j] if team not in [k for k in range(2**i) if (s[k] >> (i-1) & 1) == 0])
    
    return sorted([team for teams in dp[n] for team in teams])

n = int(sys.stdin.readline())
s = sys.stdin.read().strip()
print('\n'.join(map(str, solve(n, [int(x) for x in s]))))
