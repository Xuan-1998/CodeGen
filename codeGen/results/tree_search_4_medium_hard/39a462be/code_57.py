import sys

class Node:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.count = 0

def build_suffix_tree(s):
    root = Node('root')
    for i in range(len(s)):
        node = root
        for j in range(i, len(s)):
            c = s[j]
            if c not in node.children:
                node.children[c] = Node(c)
            node = node.children[c]
            node.count += 1
    return root

def calculate_similarity_score(node):
    count = node.count
    if count == 0:
        return 0
    else:
        return (count * 4) - len(s) - len(t)

def main():
    s = input().strip()
    t = input().strip()
    s += '$' + t
    root = build_suffix_tree(s)
    max_similarity_score = 0
    def dfs(node):
        nonlocal max_similarity_score
        if node.count > max_similarity_score:
            max_similarity_score = node.count
    dfs(root)
    print(max_similarity_score)

if __name__ == "__main__":
    main()
