def max_points(a):
    n = len(a)
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = max(dp[j] + 1 for j in range(1, i) if abs(a[i] - a[j]) == 1)

    return dp[n]

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(max_points(a))
