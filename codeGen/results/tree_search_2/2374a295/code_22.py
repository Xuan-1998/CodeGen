def solve():
    n, k = map(int, input().split())
    memo = {}
    def dp(i):
        if (i, k) in memo:
            return memo[(i, k)]
        if i > n and not is_divisible(n, i):
            return 0
        if i == 0:
            return 1
        res = 0
        for j in range(1, min(k+1, i+1)):
            if is_divisible(n, j):
                res += dp(i-j)
        memo[(i, k)] = res
        return res
    def is_divisible(n, i):
        while i > 1 and n % i == 0:
            n //= i
        return n == 1
    print(dp(n) % (10**9 + 7))

if __name__ == "__main__":
    solve()
