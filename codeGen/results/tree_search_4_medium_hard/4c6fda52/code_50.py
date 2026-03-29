def min_changes_needed(n, k, s):
    dp = [[False] * (k+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, k+1):
            if s[i-1] == 'RGB'[j%3]:
                dp[i][j] = dp[i-1][j-1]
    
    min_changes = 0
    for i in range(k, n+1):
        for j in range(k+1):
            if not dp[i][j]:
                min_changes += 1
    
    return min_changes

while True:
    try:
        n, k = map(int, input().split())
        s = input()
        print(min_changes_needed(n, k, s))
    except EOFError:
        break
