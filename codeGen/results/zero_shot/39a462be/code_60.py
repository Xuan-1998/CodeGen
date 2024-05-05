import sys

def find_lcs(A, B):
    m = len(A)
    n = len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    lcs = ""
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                lcs += A[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return lcs, len(lcs)

def similarity_score(A, B):
    m = len(A)
    n = len(B)
    max_similarity = 0
    for i in range(m + 1):
        for j in range(n + 1):
            substring_A = A[i:] if i == 0 else A[:i]
            for k in range(j + 1):
                substring_B = B[k:] if k == 0 else B[:k]
                lcs, length = find_lcs(substring_A, substring_B)
                similarity = 4 * length - (m - i) - (n - k)
                max_similarity = max(max_similarity, similarity)
    return max_similarity

def main():
    A = input().strip()
    B = input().strip()
    print(similarity_score(A, B))

if __name__ == "__main__":
    main()
