def min_cut_palindrome_partition(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j]:
                if j-i < 3:
                    dp[i][j] = True
                elif not (dp[i+1][j-1]):
                    dp[i][j] = True
    
    cuts = 0
    i = 0
    while i < n-1:
        for j in range(i, n):
            if not dp[i][j]:
                break
        if j == n-1:
            return cuts
        else:
            cuts += 1
            i = j
    
    return cuts + 1

s = input()
print(min_cut_palindrome_partition(s))
