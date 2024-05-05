def find_max_similarity():
    A = input().strip()
    B = input().strip()

    n, m = len(A), len(B)
    lcp_table = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                lcp_table[i][j] = lcp_table[i - 1][j - 1] + 1
            else:
                lcp_table[i][j] = max(lcp_table[i - 1][j], lcp_table[i][j - 1])

    similarity_score = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            common_length = lcp_table[i][j]
            similarity_score = max(similarity_score, 4 * common_length - (i + j))

    print(similarity_score)
