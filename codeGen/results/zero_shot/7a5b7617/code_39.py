# Read input from stdin
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    # Initialize a 2D array to store the number of different steady tables for each row
    dp = [[0] * (M + 1) for _ in range(N)]

    # Calculate the number of different steady tables for each row
    for i in range(1, N):
        for j in range(M + 1):
            if j <= M:
                dp[i][j] = sum(dp[k][min(j, M)] for k in range(i))
            else:
                dp[i][j] = sum(dp[k][M] for k in range(i))

    # Calculate the number of different steady tables modulo 1 000 000 000
    total = sum(sum(1 << (i - 1) * j + i // 2 % M for j in range(M + 1)) for i in range(N))
    print(total % 1000000000)

