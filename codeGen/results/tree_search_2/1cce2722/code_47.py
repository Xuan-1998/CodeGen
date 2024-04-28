def max_points():
    n = int(input())
    a = list(map(int, input().split()))
    k = 0

    for i in range(1, n):
        if a[i] == a[k]:
            k += 1
        else:
            break

    dp = [n] * n
    dp[0] = 0

    for i in range(k+2):
        for j in range(max(0, i-2), min(n, i+2)):
            if abs(a[j] - a[i]) == 1 or abs(a[j] - a[i]) == k:
                dp[j] = min(dp[j], dp[i] + 1)
            else:
                dp[j] = n

    return max(dp)

print(max_points())
