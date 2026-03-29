def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def count_diamonds(N):
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            even_sum = sum_of_digits(i + j)
            odd_sum = sum_of_digits((i - 1) + (j - 1))
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - abs(even_sum - odd_sum)

    total_diamonds = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            total_diamonds += dp[i][j]

    return total_diamonds

T = int(input())
for _ in range(T):
    N = int(input())
    print(count_diamonds(N))
