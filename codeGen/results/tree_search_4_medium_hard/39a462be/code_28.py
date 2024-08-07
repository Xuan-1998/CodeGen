def similarity_score():
    n, m = map(int, input().split())
    A = input()
    B = input()

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    max_similarity = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_similarity = max(max_similarity, 4 * (dp[i][j]) - i - j)
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print(max_similarity)

similarity_score()
