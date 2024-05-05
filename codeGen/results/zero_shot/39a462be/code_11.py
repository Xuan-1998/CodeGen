import sys
from collections import defaultdict

def solve():
    A = input().strip()
    B = input().strip()

    dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_length = dp[-1][-1]
    similarity_score = 4 * lcs_length - (len(A) + len(B))

    print(similarity_score)

solve()
