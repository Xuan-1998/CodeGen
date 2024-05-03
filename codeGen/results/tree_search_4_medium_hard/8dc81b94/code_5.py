import sys

def can_zero_array():
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = True
    
    for i in range(1, n + 1):
        for j in range(i, -1, -1):
            if arr[j - 1] == 0 or (i > 0 and not dp[i - 1][j]) or (i < n and not dp[i][j - 1]):
                dp[i][j] = True
    
    print("YES" if dp[n][0] else "NO")

while True:
    can_zero_array()
