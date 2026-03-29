import sys

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))

    dp = [[False] * (k+1) for _ in range(n+1)]

    for i in range(1, n+1):
        dp[i][0] = True

    for j in range(k-1, -1, -1):
        for i in range(1, n+1):
            children = [u for u, v in edges if v == i]
            for child in children:
                if dp[child][k-1-j]:
                    xor_values = set()
                    for node in range(n+1):
                        if node != i and node != child:
                            xor_values.add(values[node] ^ values[i])
                    if len(xor_values) == 1:
                        dp[i][j] = True
                        break

    return "YES" if dp[0][k-1] else "NO"

print(solve())
