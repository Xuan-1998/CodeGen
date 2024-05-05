def lcs_length(a, b):
    m = len(a)
    n = len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

def similarity_score(a, b):
    lcs_len = lcs_length(a, b)
    return 4 * lcs_len - (len(a) + len(b))

def maximal_similarity_score(A, B):
    max_similarities = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A) + 1):
            for k in range(len(B)):
                for l in range(k + 1, len(B) + 1):
                    a = A[i:j]
                    b = B[k:l]
                    similarity = similarity_score(a, b)
                    max_similarities = max(max_similarities, similarity)

    return max_similarities

if __name__ == "__main__":
    A = input().strip()
    B = input().strip()
    print(maximal_similarity_score(A, B))
