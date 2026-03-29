def find_max_similarity():
    n = int(input())
    m = int(input())
    A = input().strip()
    B = input().strip()

    # Create a 2D array for dynamic programming
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    max_similarity = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_similarity = max(max_similarity, 4 * (dp[i][j] - i - j))

    print(max_similarity)

find_max_similarity()
