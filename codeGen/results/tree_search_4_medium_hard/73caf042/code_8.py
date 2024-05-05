def calculate_total_diamonds(N):
    dp = [[0] * N for _ in range(N)]

    # Initialize base case: all rooms have 0 diamonds
    for j in range(N):
        dp[0][j] = 0

    total_diamonds = 0
    for i in range(1, N+1):
        even_sum = sum(int(digit) for digit in str(i) if int(digit) % 2 == 0)
        odd_sum = sum(int(digit) for digit in str(i) if int(digit) % 2 != 0)

        if i % 2 == 0:
            dp[i][N-1] = dp[i//2][N-2] + abs(even_sum - odd_sum)
        else:
            dp[i][N-1] = dp[(i+1)//2][N-2]

        total_diamonds += dp[i][N-1]

    return total_diamonds

T = int(input())
for _ in range(T):
    N = int(input())
    print(calculate_total_diamonds(N))
