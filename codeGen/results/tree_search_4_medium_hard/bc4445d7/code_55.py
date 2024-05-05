import sys
from collections import defaultdict

def solve():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    k = int(input())
    primes = list(map(int, input().split()))

    memo = defaultdict(lambda: defaultdict(int))

    def dfs(node):
        if node == 0:
            return 0
        if (node,) in memo:
            return memo[(node,)][0]

        if len(dfs.children) > 1:
            dfs.children[1] = [i for i in range(2, k // primes[0] + 1)]
            dfs.children[-1] = [k // primes[0]] * (len(dfs.children) - 1)

        res = float('inf')
        for child in dfs.children:
            for num in child:
                res = min(res, dfs(child) + len(dfs.children) * num)
        memo[(node,)][0] = res
        return res

    dfs.children = [[i for i in range(2, k // primes[0] + 1)]]
    dfs(0)

    max_sum = float('-inf')
    for node in range(n):
        for neighbor in range(node + 1, n):
            if edges.count((node, neighbor)) > 0:
                max_sum = max(max_sum, dfs(node) + dfs(neighbor))

    print(max_sum % (10**9 + 7))


if __name__ == "__main__":
    solve()
