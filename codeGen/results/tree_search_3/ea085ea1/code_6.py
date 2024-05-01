import sys

def build_suffix_tree(s):
    # Build the suffix tree for string s
    n = len(s)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edge = (s[i:j], i)
            edges.append(edge)

    edges.sort()

    def build_suffix_tree_recursive(edges, root=None):
        if root is None:
            root = {}
        for edge in edges:
            node = edge[0][0]
            if node not in root:
                root[node] = []
            root[node].append(edge)
            build_suffix_tree_recursive([edge for e in edges if e[0][0] == node], root.get(node, {}))

    build_suffix_tree_recursive(edges)

    return root

def find_common_substrings(str1, str2):
    # Find the maximum number of common non-overlapping substrings between str1 and str2
    suffix_tree_str1 = build_suffix_tree(str1)
    suffix_tree_str2 = build_suffix_tree(str2)

    max_common_substrings = 0

    def dfs(node, path):
        nonlocal max_common_substrings
        if node in suffix_tree_str1:
            for edge in suffix_tree_str1[node]:
                dfs(edge[1], path + list(edge[0]))
            return len(path)
        else:
            return 0

    for char in set(str1):
        path_len = dfs(char, [char])
        max_common_substrings = max(max_common_substrings, path_len)

    return max_common_substrings

def main():
    str1 = input().strip()
    str2 = input().strip()

    print(find_common_substrings(str1, str2))

if __name__ == "__main__":
    main()
