MOD = 998244353

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.subtree_size = 1

def add_edge(tree, u, v):
    tree[u].children.append(tree[v])
    tree[v].children.append(tree[u])

def remove_parent_links(node, parent):
    node.children = [child for child in node.children if child != parent]
    for child in node.children:
        remove_parent_links(child, node)

def calculate_subtree_sizes(node):
    for child in node.children:
        node.subtree_size += calculate_subtree_sizes(child)
    return node.subtree_size

def find_centroid(node, total_nodes):
    for child in node.children:
        if child.subtree_size > total_nodes // 2:
            return find_centroid(child, total_nodes)
    return node

def count_permutations(node):
    size = node.subtree_size
    permutations = 1
    segment_count = 0
    for child in node.children:
        child_permutations = count_permutations(child)
        permutations = (permutations * child_permutations) % MOD
        permutations = (permutations * factorial[size]) % MOD
        size -= child.subtree_size
        segment_count += 1
    return (permutations * factorial[segment_count]) % MOD

def main():
    n = int(input().strip())
    tree = [TreeNode(i) for i in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        add_edge(tree, u - 1, v - 1)
    
    remove_parent_links(tree[0], None)
    calculate_subtree_sizes(tree[0])
    centroid = find_centroid(tree[0], n)
    
    global factorial
    factorial = [1] * (n + 1)
    for i in range(2, n + 1):
        factorial[i] = (factorial[i - 1] * i) % MOD
    
    answer = count_permutations(centroid)
    print(answer)

if __name__ == "__main__":
    main()
