import sys
from typing import List, Tuple

def lcs_length(A: str, B: str) -> int:
    m, n = len(A), len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

def similarity_score(A: str, B: str) -> int:
    lcs_len = lcs_length(A, B)
    return 4 * lcs_len - len(A) - len(B)

def main() -> None:
    A = input().strip()
    B = input().strip()

    max_similarity = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A) + 1):
            substr_A = A[i:j]
            for k in range(len(B)):
                for end_k in range(k + 1, len(B) + 1):
                    substr_B = B[k:end_k]
                    lcs_len = lcs_length(substr_A, substr_B)
                    similarity = 4 * lcs_len - len(substr_A) - len(substr_B)
                    max_similarity = max(max_similarity, similarity)

    print(max_similarity)

if __name__ == "__main__":
    main()
