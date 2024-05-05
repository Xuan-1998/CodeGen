import sys

def find_prime_factors(n):
    """Find prime factors of a number"""
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def label_edges(tree_edges, prime_factors):
    """Label edges with prime factors"""
    edge_labels = []
    for u, v in tree_edges:
        product = 1
        for p in prime_factors:
            if u < v:  # assign to shorter edge
                product *= p
            else:
                product /= p
        edge_labels.append(product)
    return edge_labels

def calculate_distribution_index(tree_edges):
    """Calculate distribution index"""
    sum_paths = 0
    for i, (u, v) in enumerate(tree_edges):
        path_sum = 1
        current_node = u
        while current_node != v:
            next_edge = [(j, k) for j, k in tree_edges if j == current_node][0]
            edge_label = edge_labels[i]
            path_sum *= edge_label
            current_node = next_edge[1]
        sum_paths += path_sum
    return sum_paths

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        tree_edges = [(int(u), int(v)) for u, v in (line.split() for line in sys.stdin.readlines())[1:-1]]
        m = int(sys.stdin.readline())
        prime_factors = [int(p) for p in sys.stdin.readline().split()]
        edge_labels = label_edges(tree_edges, prime_factors)
        distribution_index = calculate_distribution_index(tree_edges)
        print(distribution_index % (10**9 + 7))

if __name__ == "__main__":
    solve()
