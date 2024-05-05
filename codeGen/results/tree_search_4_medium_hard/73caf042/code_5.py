def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                room_number = (i + j)
                even_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 == 0)
                odd_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 != 0)
                dp[i][j] = dp[i-1][j] + abs(even_sum - odd_sum) - (dp[i][j-1] if j > 0 else 0)
        total_diamonds = sum(sum(dp[i][j] for j in range(1, n+1)) for i in range(1, n+1))
        print(total_diamonds)

if __name__ == "__main__":
    solve()
