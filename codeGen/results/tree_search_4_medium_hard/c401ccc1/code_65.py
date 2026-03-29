import sys
from collections import defaultdict

def read_input():
    q = int(input())
    queries = []
    for _ in range(q):
        u, v = map(int, input().split())
        queries.append((u, v))
    return queries

def solve_queries(queries):
    dp = defaultdict(bool)
    for u, v in queries:
        if not dp[v]:
            for w in range(2**30):
                if (w & v == v) and dp[w]:
                    dp[v] = True
                    break
        if dp[v]:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    queries = read_input()
    solve_queries(queries)
