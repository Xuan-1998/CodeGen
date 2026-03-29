def find_max_similarity_score():
    A = input().strip()
    B = input().strip()

    n, m = len(A), len(B)
    dp = [[[0] * (min(n, m) + 1) for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j][0] = max(i, j) - min(i, j)
            else:
                common_length = 0
                while common_length < min(i, j) and A[i - 1 - common_length] == B[j - 1 - common_length]:
                    common_length += 1
                dp[i][j][0] = max(dp[i-1][j-1][common_length], dp[i-1][j][0], dp[i][j-1][0]) + 4 * common_length - (i + j)

    print(max([dp[i][j][0] for i in range(n + 1) for j in range(m + 1)]))
