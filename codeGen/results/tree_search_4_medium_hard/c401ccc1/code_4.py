import sys

def read_input():
    q = int(sys.stdin.readline().strip())
    queries = []
    for _ in range(q):
        u, v = map(int, sys.stdin.readline().strip().split())
        queries.append((u, v))
    return q, queries

def solve_queries(queries):
    dp = [False] * (2**30)
    dp[0] = True
    for i, j in queries:
        if any(k < i.bit_length() and not (i & (1 << k)) and dp[k] for k in range(i.bit_length()) if not (i & (1 << k))):
            dp[j] = True
    for u, v in queries:
        if dp[v]:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    q, queries = read_input()
    solve_queries(queries)
