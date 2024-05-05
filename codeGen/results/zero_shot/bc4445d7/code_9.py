import sys
from math import prod

def main():
    T = int(input())
    for _ in range(T):
        n, *edges = [int(x) for x in input().split()]
        m, *primes = [int(x) for x in input().split()]
        k = prod(primes)
        
        # Initialize the tree
        tree = [[] for _ in range(n)]
        for u, v in zip(edges, edges[1:]):
            tree[u].append(v)
            tree[v].append(u)

        # Initialize the distribution index
        dist_index = 0

        def dfs(u):
            nonlocal dist_index
            if not tree[u]:
                return k
            for v in tree[u]:
                if (u < v and prod(tree[u]) * prod(tree[v])) % k == 0:
                    k //= prod(tree[u])
                else:
                    k = prod(tree[u])
                return k + dfs(v)

        dfs(0)
        print(dist_index % (10**9 + 7))

if __name__ == "__main__":
    main()
