def count_blocks(n):
    MOD = 998244353
    dp = {(i, j): [0] * (n + 1) for i in range(n + 1)}

    for l in range(1, n + 1):
        for i in range(l - 1, -1, -1):
            for j in range(min(i + 1, l), 0, -1):
                if i < 0:
                    dp[(i, j)][l] = 1
                elif j < 0 or l < 0:
                    dp[(i, j)][l] = 0
                else:
                    if i == 0:
                        dp[(i, j)][l] = 1
                    else:
                        dp[(i - 1, j)][l] += dp[(i - 1, j)][l]
                        dp[(i, j)][l] %= MOD

    return " ".join(map(str, [dp[(n - 1, n)][i] for i in range(1, n + 1)]))

n = int(input())
print(count_blocks(n))
