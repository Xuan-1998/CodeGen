import sys

def process_queries(n, q, arr, l, r):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Initialize dp[i][0] with signs of elements from i to n
    for i in range(1, n + 1):
        if arr[i - 1] == '+':
            dp[i][0] = 1
        else:
            dp[i][0] = 0
    
    # Fill up the dp table
    for i in range(1, n + 1):
        for j in range(1, min(i + 1, r + 1)):
            if arr[j - 1] == '+':
                if dp[i - 1][j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                if dp[i - 1][j - 1]:
                    dp[i][j] = min(dp[i - 1][j - 1], 1) + 1
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], 0)
    
    # Process queries
    for i in range(q):
        l, r = map(int, sys.stdin.readline().split())
        if r < n:
            print(dp[r][0])
        else:
            print(min(dp[r][j] for j in range(l, r + 1)))

# Read input and process queries
n, q = map(int, sys.stdin.readline().split())
arr = list(sys.stdin.readline().strip())
for _ in range(q):
    l, r = map(int, sys.stdin.readline().split())
process_queries(n, q, arr, l, r)
