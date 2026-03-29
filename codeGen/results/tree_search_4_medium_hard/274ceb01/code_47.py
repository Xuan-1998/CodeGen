def min_marks_below_water_level():
    n = int(input())  # number of days
    marks_above_water = list(map(int, input().split()))  # list of marks strictly above water on each day

    dp = [[0] * (i + 1) for i in range(n)]

    for i in range(1, n):
        for k in range(i + 1):
            if k > 0:
                dp[i][k] = dp[i - 1][max(k - 1, 0)] + (i - k) * k
            else:
                dp[i][k] = sum(marks_above_water[:i])

    return min(dp[-1])  # minimum number of marks below water level when the water level is at height 0

print(min_marks_below_water_level())
