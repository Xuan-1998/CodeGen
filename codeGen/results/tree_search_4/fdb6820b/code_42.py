def count_ways_to_form_N(arr, N):
    dp = [0] * (N + 1)
    dp[0] = 1  # base case: there's one way to form 0

    for x in arr:
        for j in range(N, x - 1, -1):  # iterate from N to x-1
            dp[j] += dp[j - x]
            dp[j] %= (10**9 + 7)  # take the result modulo 10^9+7

    return dp[N]

# read input from stdin
m = int(input())
N = int(input())
arr = list(map(int, input().split()))

print(count_ways_to_form_N(arr, N))
