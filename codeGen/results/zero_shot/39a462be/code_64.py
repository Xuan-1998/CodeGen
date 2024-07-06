def calculate_similarity_score():
    # Read input strings A and B from stdin
    A = input().strip()
    B = input().strip()

    # Initialize maximum similarity score
    max_similarity_score = 0

    # Iterate over all possible substrings of A and B
    for i in range(len(A)):
        for j in range(i + 1, len(A) + 1):
            for k in range(len(B)):
                for l in range(k + 1, len(B) + 1):
                    # Calculate the similarity score for the current substrings
                    substring_A = A[i:j]
                    substring_B = B[k:l]
                    length_lcs = len(lcs(substring_A, substring_B))
                    similarity_score = 4 * length_lcs - (len(substring_A) + len(substring_B))

                    # Update maximum similarity score if necessary
                    max_similarity_score = max(max_similarity_score, similarity_score)

    # Print the maximum similarity score to stdout
    print(max_similarity_score)


def lcs(A, B):
    m, n = len(A), len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_length = max(max_length, dp[i][j])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return A[max_length]
