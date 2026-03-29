def count_permutations():
    n = int(input())
    m = list(map(int, input().split()))
    MOD = 10**9 + 7

    dp = {0: [(0,)]}

    for i in range(1, n):
        new_dp = {}
        for j in range(n - i):
            for k in range(j+1):
                if m[i] <= m[k]:
                    new_dp[(j, k)] = dp.get((k, j-k-1), [(0,)]) + [dp[(k, j-k-1)][-1] + 1]
                else:
                    new_dp[(j, k)] = ((new_dp.get((k, j-k-1), [(0,)]) or []) + [dp[(k, j-k-1)][-1] + 1],) % MOD
        dp = new_dp

    return len(dp.get((n-1, n-1), [])) % MOD

print(count_permutations())
