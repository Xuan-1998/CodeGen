def is_divisible(i, j):
    return i % j == 0

def dp(n, k):
    memo = {}
    def recursive_dp(i, k):
        if (i, k) in memo:
            return memo[(i, k)]
        if i > n or k == 0:
            return 1
        res = 0
        for j in range(2, min(i, k)+1):
            if is_divisible(i, j):
                res += recursive_dp(j-1, k-j)
        memo[(i, k)] = res % 1000000007
        return res
    return recursive_dp(n, k)

n, k = map(int, input().split())
print(dp(n, k))
