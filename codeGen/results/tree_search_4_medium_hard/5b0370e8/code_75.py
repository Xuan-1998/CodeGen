import sys

def solve():
    n, k = map(int, input().split())
    dp = [[0]*((1<<k)-1) for _ in range(n+1)]
    dp'[dp[dp[':']]] = 1
    
    for i in range(1, n+1):
        for j in range((1<<k)-1):
            if not any((a & j) != a for a in range(i)):
                if all(((a & (j >> bit)) << bit) == j for bit in range(k-1, -1, -1)):
                    dp[i][j] = 1
                else:
                    dp[i][j] = sum(dp[j'')[0] for j'' in range((1<<k)-1))
            if any(((a & (j >> bit)) << bit) != j for bit in range(k-1, -1, -1)):
                dp'[i][j] = 1
    
    print(sum(dp[n][j] for j in range((1<<k)-1)))

if __name__ == "__main__":
    solve()
