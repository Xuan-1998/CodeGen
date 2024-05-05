from collections import defaultdict

def solve():
    n, k = map(int, input().split())
    s = input()

    dp = [[[] for _ in range(k+1)] for _ in range(n+1)]
    memo = defaultdict(list)

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == 0:
            return [''] * (j+1)

        res = []
        if k <= i:
            for c in s[:min(i, k)] + (s[-1] if i > k else ''):
                res.append(c)
                yield from dfs(i-1, j-1) if len(res) == j else []

        if k > i:
            for c in s[:k]:
                res.append(c)
                yield from dfs(i, j-1)

        memo[(i, j)] = list(set([str(x) for x in res]))

    print(''.join(sorted(dfs(n, k), key=lambda x: (x[0] if x else '', len(x)))))

if __name__ == '__main__':
    solve()
