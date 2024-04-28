def max_points(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        k = i - 1
        while k >= 1 and a[k] > a[i]:
            k -= 1
        if k < 1:
            dp[i] = 1
        else:
            j = i - 1
            while j >= k and a[j] <= a[k]:
                j -= 1
            dp[i] = 1 + (i - j - 1) * (j >= k)
    return max(dp)

n = int(input())
a = list(map(int, input().split()))
print(max_points(n))
