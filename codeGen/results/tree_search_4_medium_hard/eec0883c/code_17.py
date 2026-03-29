from collections import deque

def max_gas(n, w, roads):
    memo = {}

    def dfs(city, j, w):
        if (city, j) in memo:
            return memo[(city, j)]
        if city == n - 1:  # reached the last city
            return min(w[city], j)
        memo[(city, j)] = 0
        for neighbor, c in roads[city]:
            next_j = j - c
            if next_j >= 0:
                memo[(city, j)] = max(memo[(city, j)], dfs(neighbor, next_j, w))
        return memo[(city, j)]

    return dfs(0, w[0], w)
