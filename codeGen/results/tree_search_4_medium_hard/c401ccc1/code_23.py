from functools import lru_cache

def infinite_zoo(q):
    @lru_cache(None)
    def dfs(i):
        if i == 0:
            return 1
        return 2 ** (i - 1)

    for _ in range(q):
        u, v = map(int, input().split())
        if u & v != v:
            print("NO")
        else:
            reachable = set([v])
            while v:
                v &= (v - 1)
                reachable |= {w for w in range(2**30) if w & v == v}
            if any(reachable):
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    q = int(input())
    infinite_zoo(q)
