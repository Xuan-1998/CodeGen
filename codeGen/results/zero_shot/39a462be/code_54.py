def lcs_length(A, B):
    m = len(A)
    n = len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

def similarity_score(A, B):
    return 4 * lcs_length(A, B) - (len(A) + len(B))

def max_similarity_score(A, B):
    max_score = 0

    for i in range(len(A)):
        for j in range(i + 1, len(A) + 1):
            for k in range(len(B)):
                for l in range(k + 1, len(B) + 1):
                    score = similarity_score(A[i:j], B[k:l])
                    max_score = max(max_score, score)

    return max_score

A = input().strip()
B = input().strip()
print(max_similarity_score(A, B))
