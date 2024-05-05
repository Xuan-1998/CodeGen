def lcs_length(s1, s2):
    m = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    longest, x_longest = 0, 0

    for x in range(1, len(s1) + 1):
        for y in range(1, len(s2) + 1):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x

    return longest, x_longest


def max_similarity_score(A, B):
    n = len(A)
    m = len(B)

    # Calculate LCS length and positions for all pairs of substrings
    lcs_scores = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            for k in range(m):
                for end in range(k + 1, m + 1):
                    lcs_len, _ = lcs_length(A[i:j], B[k:end])
                    score = (4 * lcs_len) - (j - i + end - k)
                    lcs_scores.append(score)

    # Return the maximum similarity score
    return max(lcs_scores)


# Read input from standard input
A = input().strip()
B = input().strip()

# Calculate and print the maximum similarity score
print(max_similarity_score(A, B))
