from bitstring import BitArray
from collections import defaultdict

def read_queries():
    q = int(input())
    queries = []
    for _ in range(q):
        u, v = map(int, input().split())
        queries.append((u, v))
    return queries

def main():
    queries = read_queries()
    dp = defaultdict(set)
    for u, v in queries:
        if v & u == v:
            dp[u].add(v)
    for query in queries:
        u, v = query
        if v & u == v:
            print("YES" if v in dp[u] else "NO")
        else:
            print("NO")

if __name__ == "__main__":
    main()
