def solve():
    a, b = map(int, input().split())
    memo = {}
    def dp(i):
        if i < 0:
            return 0
        if memo.get(i, None):
            return memo[i]
        result = (dp(i-1) + ((a >> i) ^ (b >> (i-1)))) % (10**9+7)
        memo[i] = result
        return result
    result = sum(dp(i) for i in range(a.bit_length()))
    print(result % (10**9+7))

if __name__ == "__main__":
    solve()
