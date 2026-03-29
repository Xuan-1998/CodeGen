import sys

q = int(sys.stdin.readline())

dp = [1] * (2**30)  # initialize DP table with all vertices reachable by themselves

for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    if u & v == v:  # edge from u to v
        dp[u] += dp[v]
    print("YES" if dp[v] > 0 else "NO")
