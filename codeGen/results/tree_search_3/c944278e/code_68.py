import sys

def solve():
    n = int(sys.stdin.readline())
    s = list(map(int, sys.stdin.readline().strip()))
    
    # Initialize the dp array with 2^n teams in each phase.
    dp = [[2**n] for _ in range(n + 1)]
    
    for i in range(n):
        for k in range(2):
            if k == 0:  # Losing team
                dp[i + 1][k] = sum([t for t in dp[i][1 - k] if not (s[i] & (1 << (n - i - 1)))])
            else:  # Winning team
                dp[i + 1][k] = sum([t for t in dp[i][k] if s[i]])
    
    print(' '.join(map(str, [team for team in dp[n]])))

if __name__ == "__main__":
    solve()
