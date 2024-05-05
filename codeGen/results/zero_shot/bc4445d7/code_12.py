import sys

T = int(input())  # Number of test cases
for _ in range(T):
    n = int(input())  # Number of nodes in the tree
    edges = []  # List of edge labels
    m = int(input())  # Number of prime factors in k
    primes = [int(x) for x in input().split()]  # Prime factors of k
    k = 1  # Initialize product of prime factors
    for p in primes:
        k *= p

    # Process edges
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))

    # Calculate edge labels
    edge_labels = [0] * (n - 1)
    for p in primes:
        count_p = 0
        for i, (u, v) in enumerate(edges):
            if u != v:  # Check if it's an edge
                if u == i + 1 or v == i + 1:  # If the node is on this path
                    count_p += 1
        edge_labels = [(x + 1) if (p - 1) in [y for y in range(n - 1)] else x for x in edge_labels]

    # Calculate distribution index
    distribution_index = 0
    for i, (u, v) in enumerate(edges):
        if u != v:  # Check if it's an edge
            path_sum = sum(edge_labels[:i]) + sum(edge_labels[i + 1:])
            distribution_index += path_sum

    print(distribution_index % (10**9 + 7))
