import sys

def max_gasoline(n, w, roads):
    dp = [[0] * (w[i] + 1) for i in range(n)]
    roads.sort(key=lambda x: x[2])

    for u, v, c in roads:
        for gas in range(w[u-1], -1, -1):
            if gas >= c and dp[u-1][gas-c] > 0:
                dp[v-1][gas] = max(dp[v-1][gas], dp[u-1][gas-c])
    return dp[-1][-1]

# Read inputs
n = int(input())
w = [int(x) for x in input().split()]
roads = []
for _ in range(n-1):
    u, v, c = map(int, input().split())
    roads.append((u, v, c))

print(max_gasoline(n, w, roads))
