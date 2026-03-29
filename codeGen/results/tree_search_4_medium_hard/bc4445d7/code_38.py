import heapq
from collections import defaultdict

def solve():
    T = int(input())  # number of test cases
    for _ in range(T):
        n = int(input())  # number of nodes
        edges = [list(map(int, input().split())) for _ in range(n - 1)]
        m = int(input())  # number of prime factors
        prime_factors = list(map(int, input().split()))

        # Create a tree from the given edges
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Calculate the minimum possible count of ones on each edge
        dp = [[[float('inf'), 0] for _ in range(n)] for _ in range(n)]
        dp[0][1][0] = 0

        for u, v in edges:
            for i in range(dp[u][v][0] + 1):
                if i <= dp[v][1][0]:
                    heapq.heappush(heapq.heapify((dp[u][v][0], i)))
                    break
            else:
                continue
            while heap:
                count, ones = heapq.heappop()
                for w in graph[v]:
                    if w not in graph[u]:
                        continue
                    if w != v and w != 1:
                        continue
                    dp[u][w][0] = min(dp[u][w][0], (dp[v][w][0] + count, ones))
                    dp[w][v][0] = min(dp[w][v][0], (count, ones))

        # Calculate the maximum possible distribution index
        max_distribution_index = 0
        for i in range(1, n):
            for j in range(i + 1, n):
                if not (graph[i][j]):
                    continue
                max_distribution_index += dp[0][i][0] * prime_factors[m - 1]
                m -= 1

        print(max_distribution_index % (10 ** 9 + 7))

solve()
