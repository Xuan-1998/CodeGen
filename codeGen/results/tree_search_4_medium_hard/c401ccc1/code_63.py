from collections import defaultdict

def infinite_zoo_queries():
    q = int(input())
    memo = defaultdict(bool)
    for _ in range(q):
        u, v = map(int, input().split())
        memo[v] = any((memo[j] and (u & j) == v) for j in range(2**30))
        print("YES" if memo[v] else "NO")

if __name__ == "__main__":
    infinite_zoo_queries()
