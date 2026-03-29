import heapq

def solve():
    n = int(input())
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))

    m = int(input())
    prime_factors = list(map(int, input().split()))

    # Initialize a heap with all nodes
    heap = [(0, i) for i in range(1, n + 1)]
    heapq.heapify(heap)

    edge_labels = [1] * (n - 1)
    label_sum = 1

    while heap:
        # Extract the node with the minimum value from the heap
        label_sum *= heapq.heappop(heap)[0]

        # Update edge labels based on prime factors
        for _ in range(m):
            if label_sum % prime_factors[_] == 0:
                edge_labels[edges.pop(0)] = prime_factors[_]
                break

    distribution_index = sum((i + j) * (edge_labels[i - 1] != 1) for i, j in edges)
    print(distribution_index % (10 ** 9 + 7))

if __name__ == "__main__":
    solve()
