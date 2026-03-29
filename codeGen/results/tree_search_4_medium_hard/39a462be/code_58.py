import sys
from collections import defaultdict

def build_suffix_tree(s):
    tree = defaultdict(list)
    for i, c in enumerate(reversed(s)):
        if c not in tree[i]:
            tree[i].append(c)
    return tree

def calculate_similarity_score(tree1, tree2):
    max_length = 0
    for i in sorted(tree1.keys()):
        for j in sorted(tree2.keys()):
            if i + len(tree1[i]) == j:
                common_length = min(len(tree1[i]), len(tree2[j]))
                max_length = max(max_length, common_length)
    return (4 * max_length) - (len(s1) + len(s2))

def solve():
    s1 = input().strip()
    s2 = input().strip()
    tree1 = build_suffix_tree(s1)
    tree2 = build_suffix_tree(s2)
    print(calculate_similarity_score(tree1, tree2))

if __name__ == "__main__":
    solve()
