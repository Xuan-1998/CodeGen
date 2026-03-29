def solve():
    N = int(input())
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    def f(i, j):
        if i == 0 or j == 0:
            return 0

        room_num = i + j - 1
        even_sum = sum(int(digit) for digit in str(room_num) if int(digit) % 2 == 0)
        odd_sum = sum(int(digit) for digit in str(room_num) if int(digit) % 2 != 0)

        return abs(even_sum - odd_sum) + dp[i-1][j-1]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = f(i, j)

    print(dp[N][N])

if __name__ == "__main__":
    solve()
