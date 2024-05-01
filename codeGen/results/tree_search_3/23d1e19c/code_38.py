import sys

def read_input():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    k = int(input())
    p = list(map(int, input().split()))
    return n, m, edges, k, p

def solve(n, m, edges, k, p):
    # Initialize max_recomputations array
    max_recomputations = [0] * (n + 1)

    # Set the initial value for the maximum number of recomputations needed from the start to t
    max_recomputations[0] = 0

    # Iterate over the edges in reverse order
    for i in range(k, -1, -1):
        j = p[i]
        # Update max_recomputations[j] as the minimum number of recomputations needed from all vertices reachable from j to t
        max_recomputations[j] = min(max_recomputations[j] + 1, max_recomputations[0] + 1)
        for neighbor in [neighbor for u, neighbor in edges if u == j]:
            max_recomputations[j] = min(max_recomputations[j], max_recomputations[neighbor] + 1)

    # Return the minimum and maximum number of times the shortest path needs to be recomputed
    return max_recomputations[0], max_recomputations[-1]

def main():
    n, m, edges, k, p = read_input()
    min_recomputations, max_recomputations = solve(n, m, edges, k, p)
    print(f"{min_recomputations} {max_recomputations}")

if __name__ == "__main__":
    main()
