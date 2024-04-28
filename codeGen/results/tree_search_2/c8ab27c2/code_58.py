import sys
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end_of_subsequence = False

def insert_into_trie(trie, s):
    node = trie
    for c in s:
        node = node.children[c]
    node.is_end_of_subsequence = True

def find_shortest_uncommon_subsequence(s, t):
    trie = TrieNode()
    insert_into_trie(trie, s)

    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

    shortest_length = sys.maxsize
    for i in range(len(s)):
        if not trie.children.get(s[i]).is_end_of_subsequence:
            shortest_length = min(shortest_length, dp[i][len(t)])

    return -1 if shortest_length == sys.maxsize else shortest_length

# Read input from stdin and print the answer to stdout
s = input().strip()
t = input().strip()
print(find_shortest_uncommon_subsequence(s, t))
