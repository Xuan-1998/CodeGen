def is_divisible(sub, k):
    return all(x % k == 0 for x in sub)

def count_good_subsequences(n, a):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(i):
            if is_divisible(a[j:i], j + 1):
                dp[i] += dp[j]
        dp[i] %= 10**9 + 7

    return dp[n]

n = int(input())
a = list(map(int, input().split()))
print(count_good_subsequences(n, a))
