def findShortestSubArray(S):
    n = len(S)
    S_set = set()
    
    dp = [[-1] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if ''.join(S[i - j:i]) not in S_set:
                S_set.add(''.join(S[i - j:i]))
                dp[i][j] = 0
            else:
                k = i
                while k > 0 and ''.join(S[k - j:k]) in T:
                    k -= 1
                if k == 0:
                    dp[i][j] = j + 1
                else:
                    dp[i][j] = k + 1

    res = float('inf')
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if dp[i][j] > 0 and (i == n or dp[i + 1][j] < 0) and (j == n or dp[i][j + 1] < 0):
                res = min(res, dp[i][j])
    return -1 if res == float('inf') else res
