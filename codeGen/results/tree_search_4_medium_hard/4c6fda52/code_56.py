def min_changes(n, k, s):
    dp = [[False] * (k+1) for _ in range(n)]
    
    # Initialize the first column
    for i in range(n):
        if s[i:k+i].count('R') + s[i:k+i].count('G') + s[i:k+i].count('B') == k:
            dp[i][0] = True
    
    # Fill up the table
    for j in range(1, k+1):
        for i in range(n-j):
            if (s[i+k-1] != 'R' or s[i+j-1] != 'G' or s[i+j-1] != 'B') and dp[i][j-1]:
                dp[i][j] = True
    
    # Find the maximum value, which represents the minimum number of changes
    max_changes = 0
    for i in range(n-k+1):
        if not dp[i][k]:
            max_changes = (i + k) - i
            break
    
    return n - max_changes

while True:
    try:
        n, k = map(int, input().split())
        s = input()
        print(min_changes(n, k, s))
    except EOFError:
        break
