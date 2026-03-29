def goodSubsequence(a):
    n = len(a)
    dp = [False] * (n + 1)

    def helper(i):
        if i <= 0:
            return 0
        if i > 1 and a[i] % i == 0:
            return 1
        if dp[i - 1]:
            return (dp[i - 1] + (a[i] % len(str(dp[i - 1]).count('True')) == 0)) % (10**9 + 7)
        return dp[i - 1]

    for i in range(1, n + 1):
        dp[i] = helper(i)

    return sum([int(x) for x in str(dp).split(', ')]) % (10**9 + 7)

n = int(input())
a = list(map(int, input().split()))
print(goodSubsequence(a))
