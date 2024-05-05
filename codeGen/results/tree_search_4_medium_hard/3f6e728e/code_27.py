import sys

dp = [0] * (C + 1)
dp[0] = 1  # base case: there's exactly one way to build an empty sequence

for _ in range(int(input())):  # read T test cases
    N, M, C = map(int, input().split())
    upper_radii = list(map(int, input().split()))
    lower_radii = list(map(int, input().split()))

    for i in range(C + 1):
        dp[i] = sum(dp[j] for j in range(i+1)) % (10**9 + 7)

    print(*dp, sep=' ')  # output the answer for each test case
