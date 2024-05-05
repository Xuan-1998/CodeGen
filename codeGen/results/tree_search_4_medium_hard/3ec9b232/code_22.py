def count_partitions(n):
    MOD = 10**9 + 7

    dp = [[0] * (1 << n) for _ in range(n + 1)]
    memo = {}

    def dfs(i, p):
        if i == n:
            return 1
        if p in memo:
            return memo[p]
        result = 0
        for j in range(1, n - i + 1):
            q = (p >> 1) | (1 << n - i)
            if (q >> j) & 1:
                result += dfs(i + j, q)
            else:
                result -= dfs(i + j, q)
        memo[p] = result
        return result % MOD

    result = 0
    for p in range(1 << n):
        result += dfs(0, p)
    return result % MOD

if __name__ == "__main__":
    n = int(input())
    M = list(map(int, input().split()))
    print(count_partitions(n))
