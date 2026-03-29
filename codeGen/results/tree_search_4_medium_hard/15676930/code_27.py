from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = defaultdict(lambda: defaultdict(dict))
dp[0][True][True] = a[0]

for i in range(1, n):
    for left_hungry in [True, False]:
        for right_hungry in [True, False]:
            if left_hungry and right_hungry:
                dp[i][left_hungry][right_hungry] = c[i-1]
            elif not left_hungry and not right_hungry:
                dp[i][left_hungry][right_hungry] = a[i]
            else:
                dp[i][left_hungry][right_hungry] = max(b[i-1], dp[i-1][not left_hungry][right_hungry]) + c[i]

print(dp[n-1][True][True])
