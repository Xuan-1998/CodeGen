import sys
from collections import defaultdict

def solve():
    A = input().strip()
    B = input().strip()

    # Build suffix trees for both strings
    tree_A = SuffixTree(A)
    tree_B = SuffixTree(B)

    max_similarity_score = 0

    # Iterate over all possible substrings of A and B
    for i in range(len(A)):
        for j in range(len(B)):
            k = 0
            while i + k < len(A) and j + k < len(B):
                if A[i+k] == B[j+k]:
                    k += 1
                else:
                    break

            # Calculate the similarity score using your formula
            similarity_score = 4 * k - (len(A) + len(B))
            max_similarity_score = max(max_similarity_score, similarity_score)

    print(max_similarity_score)


class SuffixTree:
    def __init__(self, string):
        self.root = {}
        self.build_tree(string)

    def build_tree(self, string):
        for i in range(len(string)):
            suffix = string[i:]
            node = self.root
            for char in suffix:
                if char not in node:
                    node[char] = defaultdict(int)
                node = node[char]
                node['end'] = i

    def query(self, pattern):
        node = self.root
        for char in pattern:
            if 'end' in node:
                return node['end']
            node = node[char]

        return -1


if __name__ == '__main__':
    solve()
