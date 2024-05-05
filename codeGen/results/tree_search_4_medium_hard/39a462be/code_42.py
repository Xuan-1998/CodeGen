import sys

def build_suffix_tree(s):
    # Build the suffix tree for string s
    tree = {}
    for i, c in enumerate(reversed(s)):
        if c not in tree:
            tree[c] = []
        tree[c].append((i, len(s) - i))
    return tree

def calculate_similarity_score(A, B):
    # Calculate the similarity score between strings A and B
    A_tree = build_suffix_tree(A)
    B_tree = build_suffix_tree(B)

    max_similarity = 0
    for k in range(max(len(A), len(B))):
        for i in A_tree:
            for j in B_tree:
                if i[1] == k and j[1] == k:
                    common_length = min(i[0], j[0])
                    similarity = 4 * common_length - (len(A) + len(B))
                    max_similarity = max(max_similarity, similarity)

    return max_similarity

A = input().strip()
B = input().strip()

print(calculate_similarity_score(A, B))
