def min_cuts(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                dp[i][j] = True
    
    cuts = 0
    last_palindromic_index = -1
    for i in range(n):
        if not dp[0][i]:
            last_palindromic_index = i
            break
    
    while last_palindromic_index < n:
        cuts += 1
        last_palindromic_index += 1
        while last_palindromic_index < n and not dp[last_palindromic_index - 1][last_palindromic_index]:
            last_palindromic_index += 1
    
    return cuts

if __name__ == "__main__":
    s = input()
    print(min_cuts(s))
