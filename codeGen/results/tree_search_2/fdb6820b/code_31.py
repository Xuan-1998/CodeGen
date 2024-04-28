import sys

def solve():
    m, N = map(int, input().split())
    nums = list(map(int, input().split()))

    # Create a dictionary to store the intermediate results
    dp = {0: 1}

    for num in nums:
        temp_dp = {}
        for i in range(N + 1):
            if i - num >= 0 and i - num in dp:
                temp_dp[i] = (temp_dp.get(i, 0) or 0) + dp[i - num]
        dp = temp_dp

    return str(dp[N]) % (10**9 + 7)

print(solve())
