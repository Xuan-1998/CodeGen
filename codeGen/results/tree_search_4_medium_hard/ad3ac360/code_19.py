def min_cuts(s):
    n = len(s)
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    
    # Initialize base cases
    dp[0][0] = True
    
    for i in range(n):
        for j in range(i, n):
            if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                dp[i][j] = True
    
    # Calculate the minimum number of cuts
    min_cuts = 0
    for i in range(n):
        while not dp[0][i]:
            min_cuts += 1
            i -= 1
    
    return min_cuts

if __name__ == "__main__":
    s = input()
    print(min_cuts(s))
