import sys

def can_delete_edges(n, k, values):
    dp = [[[0, 0]] * (k + 1) for _ in range(n)]
    memo = {}

    def dfs(i, mi, mx):
        if (i, mi, mx) in memo:
            return memo[(i, mi, mx)]

        res = [False] * (k + 1)
        for j in range(n):
            if i != j and values[j] ^ values[i] <= k:
                x = values[j] ^ values[i]
                if x < mi:
                    mi = x
                elif x > mx:
                    mx = x
                res[x % (k + 1)] = True

        memo[(i, mi, mx)] = res
        return res

    for i in range(n):
        dp[i][0] = [False, False]

    for k_ in range(1, k + 1):
        for i in range(n):
            if i > 0:
                dp[i][k_] = dfs(i, *dp[i - 1][k_])
            else:
                dp[0][k_] = [True, True]

    return 'YES' if any(dp[-1][k]) else 'NO'

def main():
    n = int(input())
    k = int(input())
    values = list(map(int, input().split()))
    print(can_delete_edges(n, k, values))

if __name__ == '__main__':
    main()
