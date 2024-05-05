import sys
from collections import defaultdict

def dfs(tree, start, visited):
    farthest = [start]
    current_distance = 0
    for neighbor in tree[start]:
        if neighbor not in visited:
            visited.add(neighbor)
            distance = dfs(tree, neighbor, visited) + 1
            if distance > current_distance:
                current_distance = distance
                farthest = [neighbor]
            elif distance == current_distance:
                farthest.append(neighbor)
    return current_distance

def find_capital_city(tree):
    n = len(tree)
    capital = max((i for i in range(n+1)), key=lambda i: dfs(tree, i, set()))
    min_edges_to_reverse = 0
    visited = set([capital])
    for neighbor in tree[capital]:
        if neighbor not in visited:
            distance = dfs(tree, neighbor, visited) + 1
            if distance > min_edges_to_reverse:
                min_edges_to_reverse = distance
    return min_edges_to_reverse

def main():
    n = int(sys.stdin.readline())
    tree = defaultdict(list)
    for _ in range(n-1):
        si, ti = map(int, sys.stdin.readline().split())
        tree[si].append(ti)

    min_edges_to_reverse = find_capital_city(tree)
    capital_cities = [i+1 for i in range(n) if dfs(tree, i, set()) == min_edges_to_reverse]
    print(min_edges_to_reverse)
    print(' '.join(map(str, capital_cities)))

if __name__ == "__main__":
    main()
