def similarity(A, B):
    n, m = len(A), len(B)
    dp = [[[-1 for _ in range(max(5000, k+1)) for k in range(max(5000, 2))] for j in range(m+1)] for i in range(n+1)]

    for k in range(k_max):
        for i in range(n-k):
            for j in range(m-k):
                if A[i+k] == B[j+k]:
                    dp[i][j][k] = (i, j, k)
                else:
                    max_score = 0
                    for x in range(i):
                        for y in range(j):
                            if i-x <= 5 and j-y <= 5:
                                max_score = max(max_score, dp[x][y][k-1])
                    dp[i][j][k] = (i, j, k), max_score

    max_score = 0
    for i in range(n+1):
        for j in range(m+1):
            if A[i:] == B[j:]:
                max_score = max(max_score, dp[i][j][len(A[i:]) - len(B[j:])] - n - m)

    return max_score
