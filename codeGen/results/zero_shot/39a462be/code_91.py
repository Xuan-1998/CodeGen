import sys

def read_input():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    A = sys.stdin.readline().strip()
    B = sys.stdin.readline().strip()
    return A, B

def lcs_length(A, B):
    # Implement a dynamic programming algorithm to find the LCS length
    # For simplicity, use the naive approach (O(n*m))
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

def calculate_similarity_score(A, B):
    lcs_length_ = lcs_length(A, B)
    similarity_score = 4 * lcs_length_ - (len(A) + len(B))
    return similarity_score

A, B = read_input()
max_similarity_score = float('-inf')
for i in range(len(A)):
    for j in range(i + 1, len(A) + 1):
        for k in range(len(B)):
            for end_k in range(k + 1, len(B) + 1):
                lcs_length_ = lcs_length(A[i:j], B[k:end_k])
                similarity_score = calculate_similarity_score(A[i:j], B[k:end_k])
                if similarity_score > max_similarity_score:
                    max_similarity_score = similarity_score
print(max_similarity_score)
