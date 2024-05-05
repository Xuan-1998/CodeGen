def minCuts(s):
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]

    # Base cases
    for i in range(n):
        dp[i][i] = True

    if s[0] == s[-1]:
        dp[0][n-1] = True

    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j] and (length <= 3 or dp[i+1][j-1]):
                dp[i][j] = True

    # Count the number of cuts needed
    cuts = 0
    for i in range(n-1):
        if not dp[0][i]:
            cuts += 1
        for j in range(i+1, n):
            if not dp[i+1][j]:
                cuts += 1

    return cuts

def main():
    s = input()
    print(minCuts(s))

if __name__ == "__main__":
    main()
