import heapq

def max_visited_vertices(n, m, T):
    # Initialize memoized dictionary
    memo = {}

    def dfs(i, t):
        if (i, t) in memo:
            return memo[(i, t)]

        # Base case: when we reach vertex n
        if i == n:
            return T + 1

        # Explore all possible routes from current vertex to vertex n
        max_visited = 0
        for _ in range(m):
            edge = list(map(int, input().split()))
            u, v, w = edge[0], edge[1], edge[2]

            # Check if there is an edge from u to v with weight w
            if u == i:
                t += w
                max_visited = max(max_visited, dfs(v, t) + 1)

        memo[(i, t)] = max_visited
        return max_visited

    return dfs(1, 0)


if __name__ == "__main__":
    n, m, T = map(int, input().split())
    print(*max_visited_vertices(n, m, T), sep='\n')
