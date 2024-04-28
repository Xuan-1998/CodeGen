def find_distinct_sums():
    n = int(input())
    values = list(map(int, input().split()))
    max_value = max(values)
    dp = [[set() for _ in range(max_value + 1)] for _ in range(n + 1)]

    def get_state(i, sum):
        return (sum, i, max_value)

    def update_dp(i, sum):
        if i == 0:
            dp[i][sum].add(0)
        else:
            prev_sum = sum
            for j in range(i - 1, -1, -1):
                prev_sum -= values[j]
                new_sum = prev_sum + values[j]
                dp[i][new_sum].update(dp[j][prev_sum])
                if new_sum > max_value:
                    break

    for i in range(n + 1):
        update_dp(i, 0)

    distinct_sums = set()
    for sum in range(max_value + 1):
        distinct_sums.update(dp[n][sum])

    print(' '.join(map(str, sorted(distinct_sums))))
