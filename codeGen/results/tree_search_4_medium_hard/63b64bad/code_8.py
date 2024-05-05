def simulate_sequence(n, a):
    dp = [[-1] * (10**9 + 1) for _ in range(n+1)]
    dp[0][0] = 0  # base case: program terminated

    for i in range(1, n+1):
        for x in range(1, min(i, 10**9) + 1):
            if x <= 0 or x > i:
                break
            y = dp[i-1][x-1]
            new_x = x + a[x-1]
            new_y = y + a[x-1]
            dp[i][new_x] = max(dp[i][new_x], new_y)
        if any(dp[i][x] == -1 for x in range(10**9, i+1)):
            return -1  # program does not terminate
    return dp[n-1][-1]

n = int(input())
a = list(map(int, input().split()))
print(simulate_sequence(n, a))
