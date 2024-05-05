import sys

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
    return n, m, edges

def find_max_beauty(n, m, edges):
    # Sort the edges by their endpoints
    edges.sort()

    # Initialize the tail and spines
    tail = []
    spines = 0

    # Iterate over the edges
    for u, v in edges:
        if len(tail) < n:  # If we haven't reached the end of the graph yet
            if not any(node in tail for node in [u, v]):  # If neither endpoint is in the tail
                if u > v:  # Swap the endpoints if necessary
                    u, v = v, u
                tail.append(v)
        else:
            if u > v and (not any(node in tail for node in [u, v])):  # If we reached the end of the graph and this edge forms a spine
                spines += 1

    return len(tail) * spines

def main():
    n, m, edges = read_input()
    beauty = find_max_beauty(n, m, edges)
    print(beauty)

if __name__ == "__main__":
    main()
