def solve():
    t = int(input())
    MOD = 10**9 + 7
    memo = {}

    def dp(k, i):
        if (k, i) not in memo:
            if k == 0:
                memo[(k, i)] = 1
            elif k > 0 and i < 2**k:
                total = sum(1 for _ in range((i ^ (2**k - 1)) // (2**k - 1) + 1))
                memo[(k, i)] = dp(k-1, i)
                if k % 2 == 0 and i < 2**(k//2):
                    total += dp(k//2, i)
                memo[(k, i)] = (total * (1 << k)) % MOD
        return memo[(k, i)]

    for _ in range(t):
        n, k = map(int, input().split())
        res = 0
        for i in range(2**k - 1):
            if dp(k, i) > 0:
                res += dp(k, i)
        print(res % MOD)

if __name__ == "__main__":
    solve()
