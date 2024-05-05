from collections import defaultdict

def solve(text, strings):
    n = len(strings)
    dp = [[float('inf')] * (len(text) + 1) for _ in range(n + 1)]
    
    # Initialize base case: no strings needed to color empty text
    dp[0][0] = 0
    
    # Fill up the table bottom-up
    for i in range(1, n + 1):
        for j in range(len(text) + 1):
            if strings[i - 1].endswith(text[j:]):
                dp[i][j] = min(dp[i][j], dp[i - 1][j - len(strings[i - 1])])
    
    # Extract the minimum number of steps and the corresponding string indices
    m = float('inf')
    w, p = [], []
    for j in range(len(text) + 1):
        if dp[n][j] != float('inf'):
            m = min(m, dp[n][j])
            while n > 0 and j - len(strings[n - 1]) >= 0:
                w.append(n)
                p.append(j - len(strings[n - 1]))
                n -= 1
                j -= len(strings[n])
    
    # Print the output
    if m == float('inf'):
        print(-1)
    else:
        print(m)
        for i in range(m):
            print(w[i], p[i])

# Read input from stdin and solve the problem
t = input().strip()
n = int(input())
strings = [input().strip() for _ in range(n)]
solve(t, strings)
