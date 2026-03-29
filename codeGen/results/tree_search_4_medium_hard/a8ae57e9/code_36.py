import sys

def solve():
    n, k, m = map(int, input().split())
    dp = [[0] * (m + 1) for _ in range(k + 1)]

    memo = {}
    total_money = 0

    for _ in range(n):
        size, amount = map(int, input().split())
        total_money += amount

        if (size, total_money) not in memo:
            for i in range(1, k + 1):
                for j in range(1, m + 1):
                    if size <= i and j >= amount:
                        dp[i][j] = max(dp[i - 1][j - amount], dp[i][j]) + amount
            memo[(size, total_money)] = 0

        accepted_requests = total_money // dp[k][m]
        total_money %= dp[k][m]

        if accepted_requests > 0:
            for _ in range(accepted_requests):
                print(f"1 {total_money}")
            print(f"{accepted_requests} {k - k}")

    print(f"{accepted_requests} {total_money}")


if __name__ == "__main__":
    solve()
