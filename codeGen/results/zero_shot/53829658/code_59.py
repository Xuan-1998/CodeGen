import sys

def find_min_edges_to_reverse(tree):
    # Perform BFS traversal to count the number of reachable nodes from each node
    max_reachable_nodes = 0
    for i in range(1, len(tree)):
        queue = [i]
        visited = set()
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                for child in tree[node]:
                    if child not in visited:
                        queue.append(child)
        max_reachable_nodes = max(max_reachable_nodes, len(visited))

    return max_reachable_nodes

def find_all_possible_capitals(tree):
    # Start by choosing node 0 as the capital and then try each other node
    possible_capitals = [(0, 0)]  # (capital, min_edges_to_reverse)
    for i in range(1, len(tree)):
        queue = [i]
        visited = set()
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                for child in tree[node]:
                    if child not in visited:
                        queue.append(child)
        min_edges_to_reverse = len(visited) - 1
        possible_capitals.append((i, min_edges_to_reverse))

    return possible_capitals

def main():
    n = int(sys.stdin.readline())
    tree = [[] for _ in range(n)]
    for _ in range(n-1):
        si, ti = map(int, sys.stdin.readline().split())
        tree[si-1].append(ti-1)
        tree[ti-1].append(si-1)

    min_edges_to_reverse = find_min_edges_to_reverse(tree)
    possible_capitals = find_all_possible_capitals(tree)

    print(min_edges_to_reverse)
    for capital, _ in possible_capitals:
        print(capital + 1)  # Convert to 0-indexed city indices

if __name__ == "__main__":
    main()
