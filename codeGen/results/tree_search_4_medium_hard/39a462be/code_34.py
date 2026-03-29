from collections import defaultdict

def build_suffix_tree(s):
    # Build a suffix tree for string s
    suffixes = [s[i:] for i in range(len(s))]
    suffixes.sort()
    tree = defaultdict(list)
    for suff in suffixes:
        node = tree['root']
        for char in suff:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['leaf'] = True
    return tree

def calculate_similarity(dp, i, j):
    # Calculate the similarity score based on the number of nodes at the same level in the suffix trees
    n1 = len(dp[0][j])
    n2 = len(dp[i][0])
    if i == 0 or j == 0:
        return max(0, min(i, j))
    else:
        return 4 * (dp[i-1][j-1] - (n1 + n2)) + dp[i-1][j] + dp[i][j-1]

def solve():
    # Read the input strings
    A = input().strip()
    B = input().strip()

    # Initialize a 2D table to store the maximum similarity scores for substrings of lengths i and j
    n, m = len(A), len(B)
    dp = [[0] * (m+1) for _ in range(n+1)]

    # Build suffix trees for strings A and B
    treeA = build_suffix_tree(A + '$' + '#' + B[::-1])
    treeB = build_suffix_tree('#' + B + '$' + A[::-1])

    # Calculate the maximum similarity scores for substrings of lengths i and j
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = calculate_similarity(dp, i, j)

    # Print the answer
    print(max([max(row) for row in dp]))

if __name__ == "__main__":
    solve()
