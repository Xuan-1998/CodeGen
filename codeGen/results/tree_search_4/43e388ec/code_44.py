def solve():
    a, b = map(int, input().split())
    memo = {0: 0}

    def dp(i):
        if i not in memo:
            memo[i] = (dp(i-1) + ((a >> i) ^ (b >> (i-1))) % (10**9+7)) % (10**9+7)
        return memo[i]

    print(sum(dp(i) for i in range(a.bit_length())) % (10**9+7))

solve()
