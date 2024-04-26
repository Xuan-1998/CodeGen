import sys
from collections import defaultdict

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.lengths = []

    def add_child(self, child, length):
        self.children.append(child)
        self.lengths.append(length)

def dfs(node, parent, depth, node_depths):
    node_depths[node.value] = depth
    max_depth = depth
    max_node = node
    for child, length in zip(node.children, node.lengths):
        if child != parent:
            new_depth, new_node = dfs(child, node, depth + length, node_depths)
            if new_depth > max_depth:
                max_depth = new_depth
                max_node = new_node
    return max_depth, max_node

def find_diameter(root):
    node_depths = defaultdict(int)
    _, farthest_node = dfs(root, None, 0, node_depths)
    diameter, _ = dfs(farthest_node, None, 0, node_depths)
    return diameter

def main():
    n = int(sys.stdin.readline().strip())
    towns = [Node(i) for i in range(n)]
    for _ in range(n):
        u, v, l = map(int, sys.stdin.readline().strip().split())
        towns[u-1].add_child(towns[v-1], l)
        towns[v-1].add_child(towns[u-1], l)

    root = towns[0]
    diameter = find_diameter(root)
    print(diameter)

if __name__ == "__main__":
    main()
