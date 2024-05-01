import sys
from collections import defaultdict

def build_suffix_tree(s):
    tree = defaultdict(list)
    for i, c in enumerate(reversed(s)):
        node = [c]
        parent = None
        while True:
            if not parent or len(parent) < 2 * (i + 1):
                parent = [None] * (2 * (i + 1))
            pos = 0
            for j, cc in enumerate(reversed(node)):
                pos += ord(cc) - ord('a')
                if pos >= len(parent):
                    break
                node.append(parent[pos])
            else:
                break
        tree[tuple(node)] = parent
    return tree

def find_common_substrings(str1, str2):
    suffix_tree1 = build_suffix_tree(str1)
    suffix_tree2 = build_suffix_tree(str2)

    common_substrings = set()
    for node in suffix_tree1:
        if tuple(node) in suffix_tree2:
            common_substrings.add(''.join(reversed(node)))
    return len(common_substrings)

n = int(input())
str1 = input().strip()
str2 = input().strip()

print(find_common_substrings(str1, str2))
