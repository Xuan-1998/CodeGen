from collections import defaultdict

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        dp = [0] * (n + 1)
        sum_arr = sum(arr)

        for i in range(1, n + 1):
            left_sum = sum(arr[:i])
            right_sum = sum_arr - left_sum
            if left_sum == right_sum:
                dp[i] = 1
            else:
                dp[i] = max(dp[i-1], 1 + (dp.get(i//2, 0) if i % 2 == 0 else 0))

        print(max(0, dp[-1]))

solve()
