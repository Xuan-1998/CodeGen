from collections import defaultdict

def solve():
    n = int(input())
    tree = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, input().split())
        tree[u].append(v)

    memo = {0: 0}
    parent = {0: None}
    min_edges = 0

    def dfs(i):
        if i not in memo:
            memo[i] = float('inf')
            for j in tree[i]:
                if parent[j] is None:
                    parent[j] = i
                    memo[i] = min(memo[i], dfs(j) + 1)
        return memo[i]

    capitals = set()
    for i in range(1, n):
        if dfs(i) == dfs[0]:
            capitals.add(i)

    print(min(dfs(i) for i in range(1, n)))
    print('\n'.join(map(str, sorted(list(capitals)))))

if __name__ == "__main__":
    solve()
