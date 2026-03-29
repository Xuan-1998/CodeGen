import sys

def solve():
    n = int(sys.stdin.readline())
    roads = []
    for _ in range(n-1):
        a, b = map(int, sys.stdin.readline().split())
        roads.append((a, b))

    dp = [[float('inf')] * (n) for _ in range(n)]
    for p in range(n):
        if p == 0:
            for i in range(1, n):
                dp[i][p] = 1
        else:
            for i in range(1, n):
                for j in roads:
                    if i == j[1]:
                        dp[i][p] = min(dp[i][p], dp[j[0]][p-1] + (1 if p > 0 else 2))

    min Roads = float('inf')
    capitals = []
    for i in range(1, n):
        roads_to_reach_i = dp[i][-1]
        if roads_to_reach_i < min_roads:
            min_roads = roads_to_reach_i
            capitals = [i]

    print(min_roads)
    print(*capitals)

solve()
