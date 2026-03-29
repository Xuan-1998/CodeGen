import heapq
import math

def solve():
    n = int(input())
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    m = int(input())
    prime_factors = list(map(int, input().split()))
    k = math.prod(prime_factors)
    
    distribution_indices = {}
    for edge in edges:
        u, v = edge
        path_sum = 0
        visited = {u}
        queue = [(1, u)]
        
        while queue:
            p, node = queue.pop(0)
            if node == v:
                break
            if node not in visited:
                visited.add(node)
                for neighbor in edges:
                    if neighbor[0] == node and neighbor[1] not in visited:
                        queue.append((p*next_prime_factor(), neighbor[1]))
        
        path_sum = p
        distribution_indices[edge] = path_sum
    
    max_distribution_index = 0
    for edge1, edge2 in zip(edges[:-1], edges[1:]):
        path_sum1 = distribution_indices[edge1]
        path_sum2 = distribution_indices[edge2]
        max_distribution_index += (path_sum1 + path_sum2)
    
    print(max_distribution_index % (10**9 + 7))

def next_prime_factor():
    p = 2
    while True:
        if is_prime(p):
            return p
        p += 1

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

solve()
