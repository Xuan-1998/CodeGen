import sys

def solve_case():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    last_added = [0] * (n + 1)
    
    for i in range(2, n + 1):
        s = 0
        for j in range(i - 1, -1, -1):
            s ^= arr[j]
            dp[i][j] = max(s ^ x, dp[i-1][j-1] + (arr[j] ^ x) if last_added[j-1] else 0)
            last_added[i] = j
    return dp[-1][-1]

for _ in range(int(input())):
    print(solve_case())
