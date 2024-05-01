def distinct_sums(a):
    N = len(a)
    max_sum = sum(a)
    dp = [[[] for _ in range(max_sum + 1)] for _ in range(N + 1)]

    for i in range(1, N + 1):
        for s in range(max_sum + 1):
            if i > N or s > max_sum:
                continue
            if s == 0:
                dp[i][s] = [0]
            elif a[i - 1] <= s:
                dp[i][s] = (dp[i-1][s-a[i-1]] + [a[i-1]]) if dp[i-1][s-a[i-1]] else []
                dp[i][s].extend(dp[i-1][s])
            else:
                dp[i][s] = dp[i-1][s]

    return sorted(set(sum(s) for s in [item for sublist in dp[N] for item in sublist]))

# Example usage
a = list(map(int, input().split()))
print(*distinct_sums(a), sep=' ')
