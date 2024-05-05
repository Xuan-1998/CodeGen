def lcs(A, B):
    dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]

def similarity_score(A, B):
    lcs_length = lcs(A, B)
    total_length = len(A) + len(B)
    return 4 * lcs_length - total_length

def max_similarity_score(A, B):
    max_score = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A) + 1):
            for k in range(len(B)):
                for l in range(k + 1, len(B) + 1):
                    score = similarity_score(A[i:j], B[k:l])
                    max_score = max(max_score, score)
    return max_score

A = input()
B = input()
print(max_similarity_score(A, B))
