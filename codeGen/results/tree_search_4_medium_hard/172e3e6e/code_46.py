import sys

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    total = [0] * (n + 1)
    
    for i in range(1, n + 1):
        for j in range(i, -1, -1):
            if all(k % (i + 1) == 0 and a[k] // (k + 1) % (k + 1) == 0 for k in range(j, i)):
                dp[i][j] = dp[j-1][j-1]
    
    for i in range(n + 1):
        total[i] = sum(dp[i])
    
    print(sum(total) % (10**9 + 7))

if __name__ == "__main__":
    solve()
