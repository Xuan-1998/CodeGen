from collections import defaultdict
import sys

def solve():
    n = int(input())
    adj_list = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, input().split())
        adj_list[u].append(v)

    dp = [float('inf')] * (n+1)
    dp[0] = 0
    root = 1

    for i in range(2, n+1):
        if len(adj_list[i-1]) == 0:
            root = i
            break

    for i in range(1, n+1):
        if i != root:
            dp[i] = min(dp[j] + 1 for j in adj_list[i-1])

    ans = dp[n]
    capital_cities = [i for i in range(n) if len(adj_list[i]) == 0][0]

    print(ans)
    print(capital_cities+1)

if __name__ == "__main__":
    solve()
