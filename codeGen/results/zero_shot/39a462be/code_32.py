import sys

def find_max_similarity_score():
    A = input().strip()
    B = input().strip()

    max_score = 0

    for i in range(len(A)):
        for j in range(i + 1, len(A) + 1):
            for k in range(len(B)):
                for l in range(k + 1, len(B) + 1):
                    # Generate substrings A[i:j] and B[k:l]
                    substring_A = A[i:j]
                    substring_B = B[k:l]

                    # Compute LCS length using dynamic programming
                    lcs_length = 0
                    m = len(substring_A)
                    n = len(substring_B)
                    dp = [[0] * (n + 1) for _ in range(m + 1)]

                    for x in range(1, m + 1):
                        for y in range(1, n + 1):
                            if substring_A[x - 1] == substring_B[y - 1]:
                                dp[x][y] = dp[x - 1][y - 1] + 1
                            else:
                                dp[x][y] = max(dp[x - 1][y], dp[x][y - 1])

                    lcs_length = dp[m][n]

                    # Calculate similarity score
                    score = 4 * lcs_length - (j - i + l - k)

                    # Update maximum score if necessary
                    max_score = max(max_score, score)

    print(max_score)

if __name__ == "__main__":
    find_max_similarity_score()
