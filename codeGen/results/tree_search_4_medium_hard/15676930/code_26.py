import sys

def max_joys(a, b, c):
    n = len(a)
    dp = [[[0] * 2 for _ in range(2)] for _ in range(n+1)]

    # Base case: only one hare
    dp[0][0][0] = a[0]
    dp[0][0][1] = b[0]
    dp[0][1][0] = c[0]

    for i in range(1, n):
        for left_hungry in (0, 1):
            for right_hungry in (0, 1):
                # Consider all possible feed decisions
                not_fed = dp[i-1][left_hungry][right_hungry]
                fed_left = dp[i-2][left_hungry ^ 1][right_hungry] + a[i]
                fed_right = dp[i-2][left_hungry][right_hungry ^ 1] + c[i]
                fed_both = dp[i-2][0][0] + b[i]

                # Update the maximum joy value
                dp[i][left_hungry][right_hungry] = max(not_fed, fed_left, fed_right, fed_both)

    return dp[-1][-1][-1]

# Read input from stdin
n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

print(max_joys(a, b, c))
