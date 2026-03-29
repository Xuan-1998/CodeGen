def countWays(s, a):
    n = len(s)
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(min(i, 26), -1, -1):
            if ord(s[i-1]) - 97 == j:
                dp[i][j] = max(dp[i-1][k] * a[j] + k for k in range(1, i//a[j]+1))
            else:
                dp[i][j] = dp[i-1][j]
    
    ways = sum(dp[n][i] for i in range(n+1)) % (10**9 + 7)
    longestSubstrLength = max(k for i in range(n+1) for k in range(1, n//a[ord(s[i-1])-97]+1))
    minSubstrs = len(s)

    print(ways)
    print(longestSubstrLength)
    print(minSubstrs)

if __name__ == "__main__":
    n = int(input())
    s = input()
    a = [int(x) for x in input().split()]
    countWays(s, a)
