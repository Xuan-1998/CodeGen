def total_diamonds(N):
    dp = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            se = sum(int(digit) for digit in str(i * (i + 1) // 2 + j + 1) if int(digit) % 2 == 0)
            so = sum(int(digit) for digit in str(i * (i + 1) // 2 + j + 1) if int(digit) % 2 != 0)

            dp[i][j] = abs(se - so)

    return sum(sum(dp[i]) for i in range(N))

T = int(input())
for _ in range(T):
    N = int(input())
    print(total_diamonds(N))
