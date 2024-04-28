def is_divisible(n, k):
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return False
    return True

def count_good_sequences(n, k):
    memo = {}
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i > n or not is_divisible(n, i):
            return 0
        if j == 1:
            return 1
        ans = 0
        for div in range(2, min(i + 1, k - j + 1) + 1):
            if is_divisible(n, div) and dp(i - div, j - 1):
                ans += dp(i - div, j - 1)
        memo[(i, j)] = ans
        return ans

    return dp(k, k) % 10000007

n, k = map(int, input().split())
print(count_good_sequences(n, k))
