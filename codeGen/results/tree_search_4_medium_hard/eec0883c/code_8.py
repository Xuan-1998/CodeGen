import sys

def max_gas(n, w, roads):
    dp = [0] * n
    for i in range(1, n):
        dp[i] = min(w[i-1], dp[roads[i-1][0]] + roads[i-1][2])
    return dp[-1]

if __name__ == "__main__":
    n = int(input())
    w = list(map(int, input().split()))
    roads = []
    for _ in range(n-1):
        u, v, c = map(int, input().split())
        roads.append((u-1, v-1, c))
    print(max_gas(n, w, roads))
