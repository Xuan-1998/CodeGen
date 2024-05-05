from collections import deque

def infinite_zoo(u, v):
    # BFS algorithm
    queue = deque([(u, [u])])
    visited = set([u])

    while queue:
        node, path = queue.popleft()

        for next_node in range(2**30):
            if (node & next_node) == next_node and next_node not in visited:
                if next_node == v:
                    return "YES"
                visited.add(next_node)
                queue.append((next_node, path + [next_node]))

    return "NO"


def main():
    q = int(input())
    for _ in range(q):
        u, v = map(int, input().split())
        print(infinite_zoo(u, v))


if __name__ == "__main__":
    main()
