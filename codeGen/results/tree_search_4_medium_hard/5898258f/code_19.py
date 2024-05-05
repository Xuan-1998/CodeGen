import sys

def solve():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    
    dp = [[0] * (x + 1) for _ in range(n + 1)]
    
    for i in range(2, n + 1):
        for j in range(x + 1):
            if j <= 0:
                dp[i][j] = dp[i-1][j]
            else:
                xor_sum = 0
                for k in range(i):
                    xor_sum += (arr[k] ^ arr[k+1])
                dp[i][j] = max(dp[i-1][j], dp[i-1][x-j] + xor_sum)
    
    print(dp[n][x])

if __name__ == "__main__":
    solve()
