def is_divisible(i, j):
    while j % i == 0:
        i += 1
    return i

def dp(n, k):
    memo = {}
    def helper(i, k):
        if (i, k) in memo:
            return memo[(i, k)]
        if i > n or k == 0:
            return 1
        res = 0
        for j in range(2, min(i, k)+1):
            res += helper(j-1, k-j)*is_divisible(i, j)
        memo[(i, k)] = res % 1000000007
        return memo[(i, k)]
    return helper(1, k)

n, k = map(int, input().split())
print(dp(n, k))
