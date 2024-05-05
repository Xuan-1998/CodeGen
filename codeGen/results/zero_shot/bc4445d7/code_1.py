import sys
from collections import defaultdict

def read_input():
    T = int(input())
    for _ in range(T):
        n = int(input())
        edges = []
        for i in range(n-1):
            u, v = map(int, input().split())
            edges.append((u, v))
        m = int(input())
        prime_factors = list(map(int, input().split()))
        yield T, n, edges, m, prime_factors

def calculate_distribution_index(T, n, edges, m, prime_factors):
    for _ in range(T):
        tree_edges = defaultdict(dict)
        for edge in edges:
            u, v = edge
            tree_edges[u][v] = 1
            tree_edges[v][u] = 1
        
        # calculate f(u, v) for all pairs (u, v)
        f_values = {}
        for node in range(1, n+1):
            for neighbor in range(node+1, n+2):
                if (node, neighbor) not in tree_edges:
                    continue
                path_sum = 0
                current_node = node
                while True:
                    next_node = [neighbor for neighbor in range(1, n+1) if f_values.get((current_node, neighbor), None) is not None][0]
                    path_sum += prime_factors[tree_edges[current_node].get(next_node, -1)]
                    if current_node == next_node:
                        break
                    current_node = next_node
                f_values[(node, neighbor)] = f_values.get((neighbor, node), 0) + path_sum
        
        distribution_index = sum(sum(f_values.get((i, j), 0) for j in range(i+1, n+1)) for i in range(1, n))
        
        print(distribution_index % (10**9 + 7))

if __name__ == "__main__":
    for T, n, edges, m, prime_factors in read_input():
        calculate_distribution_index(T, n, edges, m, prime_factors)
