import sys

def read_input():
    A = input().strip()
    B = input().strip()
    return A, B

def calculate_similarity(A, B):
    n = len(A)
    m = len(B)

    # Build suffix trees for both strings
    tree_A = {}
    tree_B = {}

    for i in range(n):
        for j in range(m):
            if A[i] == B[j]:
                node = (i, j)
                if node not in tree_A:
                    tree_A[node] = []
                if node not in tree_B:
                    tree_B[node] = []
                tree_A[node].append(node)
                tree_B[node].append(node)

    max_similarity = 0
    for depth in range(max(n, m)):
        nodes_A = [node for node in tree_A if len(node) == depth]
        nodes_B = [node for node in tree_B if len(node) == depth]

        for node_A in nodes_A:
            for node_B in nodes_B:
                k = 0
                while node_A and node_B:
                    i, j = node_A[0], node_B[0]
                    if A[i] == B[j]:
                        k += 1
                        node_A = node_A[1:]
                        node_B = node_B[1:]
                    else:
                        break

                max_similarity = max(max_similarity, 4 * k - n - m)

    return max_similarity

A, B = read_input()
print(calculate_similarity(A, B))
