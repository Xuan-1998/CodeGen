def shortestSubsequence(s1: str, s2: str):
    n = len(s1)
    m = len(s2)

    dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = i

    for k in range(m+1):
        if s2[k-1] == s1[0]:
            dp[0][k] = 0
        else:
            dp[0][k] = -1

    for i in range(1, n+1):
        for k in range(1, m+1):
            if s1[i-1] == s2[k-1]:
                if dp[i-1][k-1] != -1:
                    dp[i][k] = dp[i-1][k-1]
                else:
                    dp[i][k] = i
            else:
                dp[i][k] = i

    for k in range(m+1):
        if dp[n][k] == n:
            return -1
        else:
            return dp[n][k]

if __name__ == "__main__":
    s1, s2 = input().split()
    print(shortestSubsequence(s1, s2))
