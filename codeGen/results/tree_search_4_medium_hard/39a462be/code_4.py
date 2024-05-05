from sys import stdin

def solve():
    A = stdin.readline().strip()
    B = stdin.readline().strip()

    dp = [[[0] * (len(B) + 1) for _ in range(len(A) + 1)] for _ in range(max(len(A), len(B)) + 1)]

    for i in range(1, max(len(A), len(B)) + 1):
        for j in range(1, min(i, len(B)) + 1):
            for k in range(1, min(i, len(A)) + 1):
                if A[k - 1] == B[j - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k])

    score = 0
    for i in range(len(A)):
        for j in range(len(B)):
            for k in range(i + 1, len(A) + 1):
                for p in range(j + 1, len(B) + 1):
                    length_of_longest_common_subsequence = dp[k][p][min(k, p)]
                    similarity_score = 4 * length_of_longest_common_subsequence - (k + p)
                    score = max(score, similarity_score)

    return score

print(solve())
