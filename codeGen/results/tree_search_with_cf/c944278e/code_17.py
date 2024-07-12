python
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    s = data[1]
    
    size = 2 ** n
    dp = [[0] * size for _ in range(n + 1)]
    
    # Initialize the base case
    for j in range(size):
        dp[0][j] = j + 1
    
    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(size >> i):
            if s[i - 1] == '0':
                dp[i][j] = min(dp[i - 1][2 * j], dp[i - 1][2 * j + 1])
            else:
                dp[i][j] = max(dp[i - 1][2 * j], dp[i - 1][2 * j + 1])
    
    # The result is the sorted list of possible values in dp[n][0]
    result = sorted(set(dp[n][:]))
    
    print(" ".join(map(str, result)))


