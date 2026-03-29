import sys

def read_input():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        edges = []
        for _ in range(n - 1):
            u, v = map(int, sys.stdin.readline().split())
            edges.append((u - 1, v - 1))
        m = int(sys.stdin.readline())
        primes = list(map(int, sys.stdin.readline().split()))
        yield n, edges, m, primes

def build_tree(edges):
    adj_list = [[] for _ in range(n)]
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list

def calculate_product(adj_list):
    product = 1
    for edge in edges:
        product *= edge[1]
    return product

for n, edges, m, primes in read_input():
    # Your code here
    pass
