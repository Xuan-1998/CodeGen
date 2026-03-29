import sys

def find_lcs(A, B):
    m, n = len(A), len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

def calculate_similarity_score(A, B):
    lcs_length = find_lcs(A, B)
    return 4 * lcs_length - (len(A) + len(B))

def find_max_similarity_score(A, B):
    max_score = 0
    for i in range(len(A)):
        for j in range(len(B)):
            substring_A = A[i:]
            substring_B = B[j:]
            score = calculate_similarity_score(substring_A, substring_B)
            if score > max_score:
                max_score = score
    return max_score

A = input()
B = input()
print(find_max_similarity_score(A, B))
