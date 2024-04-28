def count_good_sequences():
    n, k = map(int, input().split())
    memo = {}

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if j == 1:
            return 1
        res = 0
        for d in range(2, i + 1):
            if i % d == 0 and j % d == 0:
                res += dfs(d, j // d)
        memo[(i, j)] = res
        return res

    total = 0
    for i in range(1, n + 1):
        total += dfs(i, k)
    print(total % 1000000007)

count_good_sequences()
