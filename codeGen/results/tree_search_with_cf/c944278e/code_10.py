python
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    s = data[1]
    
    from collections import defaultdict
    
    # Initialize dp table
    dp = [defaultdict(set) for _ in range(n + 1)]
    
    # Base case: dp[0][j] contains {j+1}
    for j in range(2 ** n):
        dp[0][j].add(j + 1)
    
    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(0, 2 ** n, 2 ** i):
            for k in range(2 ** (i - 1)):
                if s[i - 1] == '0':
                    dp[i][j].update(min(dp[i - 1][j + k], dp[i - 1][j + k + 2 ** (i - 1)]))
                else:
                    dp[i][j].update(max(dp[i - 1][j + k], dp[i - 1][j + k + 2 ** (i - 1)]))
    
    # Extract and sort the final answer
    result = sorted(dp[n][0])
    print(" ".join(map(str, result)))


