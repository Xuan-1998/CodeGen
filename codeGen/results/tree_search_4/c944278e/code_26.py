import sys

def solve():
    n = int(sys.stdin.readline())
    s = list(map(int, sys.stdin.read().strip()))
    
    dp = [[[False for _ in range(2**n)] for _ in range(2**n)] for _ in range(n+1)]
    
    # Initialize base cases
    for j in range(2**n):
        for k in range(2**n):
            if s[0] == 1 and (k >> 0) & 1:
                dp[0][j][k] = True
    
    # Update DP table
    for i in range(n-1, -1, -1):
        for j in range(2**n):
            for k in range(2**n):
                if s[i] == 1 and (k >> 0) & 1:
                    dp[i][j][k] = any(dp[i+1][(j>>((i+1)%n))&(1<<((i+1)%n))] and ((k >> i) & 1))
    
    # Find winning teams
    winners = []
    for j in range(2**n):
        if any(dp[n-1][j][k] for k in range(2**n)):
            winners.append(j)
    
    print(*sorted(winners), sep='\n')

if __name__ == "__main__":
    solve()
