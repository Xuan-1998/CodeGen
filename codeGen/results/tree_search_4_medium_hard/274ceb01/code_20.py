def min_marks_below_water(n, marks):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if marks[i - 1] >= i:
            dp[i] = 0
        else:
            dp[i] = dp[i - 1] + (i - marks[i - 1])
    return dp[n]

n = int(input())
marks = list(map(int, input().split()))
print(min_marks_below_water(n, marks))
