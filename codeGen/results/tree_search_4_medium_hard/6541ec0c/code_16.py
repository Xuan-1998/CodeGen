import sys
from collections import defaultdict

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    tree = defaultdict(list)
    
    for _ in range(n - 1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    dp = [[False] * (k + 1) for _ in range(n + 1)]

    for i in range(2, n + 1):
        for j in range(k + 1):
            if values[i - 1] == values[0]:
                dp[i][j] = True
            else:
                for child in tree[i]:
                    if not dp[child][j - 1]:
                        break
                else:
                    dp[i][j] = True

    print("YES" if dp[n][k] else "NO")

if __name__ == "__main__":
    solve()
