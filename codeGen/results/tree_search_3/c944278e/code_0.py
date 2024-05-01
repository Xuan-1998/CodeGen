import sys

def solve():
    n = int(sys.stdin.readline())
    s = list(map(int, sys.stdin.readline().split()))
    
    dp = [[0] * (1 << n) for _ in range(n)]
    
    for i in range(1, n):
        for j in range(1 << n):
            if s[i - 1] == 1:  # Team j wins this round
                for k in range(1 << n):
                    dp[i][j | k] += dp[i - 1][k]
            else:  # Team j loses this round
                dp[i][j] -= 1
    
    winning_teams = [i for i in range(1 << n) if dp[n - 1][i]]
    
    print('\n'.join(map(str, sorted(winning_teams))))

if __name__ == "__main__":
    solve()
