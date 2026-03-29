def min_cuts(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j-i < 2 or dp[i+1][j-1]):
                dp[i][j] = True
    
    cuts = 0
    last_palindrome_end = 0
    for i in range(n):
        if not dp[0][i]:
            cuts += 1
            last_palindrome_end = i
    return cuts

if __name__ == "__main__":
    s = input()
    print(min_cuts(s))
