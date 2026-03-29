def count_ways(p):
    dp = {0: 1}
    for i in range(1, n+1):
        if p.get(i-1) is None:
            dp[i] = dp[i-1] + (dp.get(i-2, 0) if i >= 2 else 0)
        else:
            j = p[i-1]
            dp[i] = min(dp.get(i-1, float('inf')), dp.get(j, float('inf'))) + (i % 2 == 0)
    return dp[n+1]

if __name__ == "__main__":
    n = int(input())
    p = {}
    for _ in range(n):
        i, j = map(int, input().split())
        p[i-1] = j
    print(count_ways(p))
