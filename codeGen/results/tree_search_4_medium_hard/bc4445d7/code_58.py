# BEGIN SOLUTION
import heapq
from collections import defaultdict

def solve():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n-1)]
    m = int(input())
    primes = list(map(int, input().split()))

    # Pre-compute prime factors and their powers
    prime_factors = {prime: 0 for prime in primes}
    for i, prime in enumerate(primes):
        for j in range(i+1, len(primes)):
            if prime * primes[j] == m:
                break
        else:
            continue
        prime_factors[prime] += 1

    # Create a graph with edge labels
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append((v, [i+1 for i in range(len(primes))]))
        graph[v].append((u, [i+1 for i in range(len(primes))]))

    # Dynamic programming to compute the maximum possible distribution index
    memo = {}
    def dfs(node):
        if node not in memo:
            memo[node] = 0
            for child, labels in graph[node]:
                memo[node] += dfs(child) + sum(labels)
        return memo[node]

    # Compute the maximum possible distribution index of the entire tree
    max_distribution_index = 0
    for node in range(1, n):
        max_distribution_index = max(max_distribution_index, dfs(node))

    # Print the result modulo 10^9 + 7
    print((max_distribution_index + 1) % (10**9 + 7))

# END SOLUTION
