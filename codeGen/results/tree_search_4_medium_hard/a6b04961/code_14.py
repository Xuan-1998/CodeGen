from collections import defaultdict

def hedgehog_beauty(n, m, edges):
    # Initialize the dictionaries with base cases: if the tail length is 1 or less, there are no spines formed.
    even_tails = {i: 0 for i in range(2)}
    odd_tails = {i: 0 for i in range(1)}

    for edge in edges:
        u, v = edge
        # For each edge, update the state by considering all possible extensions of the current tail.
        if u not in even_tails or v not in even_tails:
            if u < n // 2:  # Edge connects to an odd-indexed vertex in the tail
                for i in range(max(even_tails) + 1):
                    if (i + 1) * 2 <= v < (i + 2) * 2:
                        even_tails[i] = max(even_tails.get(i, 0), odd_tails.get((v - u) // 2, 0))
            else:  # Edge connects to an even-indexed vertex in the tail
                for i in range(max(odd_tails) + 1):
                    if (i * 2) <= v < ((i + 1) * 2):
                        odd_tails[i] = max(odd_tails.get(i, 0), even_tails.get((v - u) // 2, 0))

    # Return the maximum value from both dictionaries, which represents the maximum possible beauty of a hedgehog.
    return max(even_tails.values(), odd_tails.values())

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
print(hedgehog_beauty(n, m, edges))
