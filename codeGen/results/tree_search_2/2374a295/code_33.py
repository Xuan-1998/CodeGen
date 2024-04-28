def is_divisible(a, b):
    return a % b == 0

def dp(n, k):
    memo = {}
    def recurse(i, k):
        if (i, k) in memo:
            return memo[(i, k)]
        if i > n or k == 0:
            return 1
        result = 0
        for j in range(2, min(i, k)+1):
            if is_divisible(i, j):
                result += recurse(j-1, k-j)
        memo[(i, k)] = result
        return result
    return recurse(n, k) % 1000000007

n, k = map(int, input().split())
print(dp(n, k))
