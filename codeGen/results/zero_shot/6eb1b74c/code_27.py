import sys

test_cases = []
while True:
    t = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    s = [sys.stdin.readline().strip() for _ in range(n)]
    test_cases.append((t, n, s))

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_string_end = False

def build_trie(strings):
    root = TrieNode()
    for s in strings:
        node = root
        for c in s:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_string_end = True
    return root

trie_root = build_trie([s_1, s_2, ..., s_n])

def find_longest_prefix(text, trie_root):
    node = trie_root
    prefix_len = 0
    while True:
        next_char = text[prefix_len]
        if next_char not in node.children:
            return prefix_len
        node = node.children[next_char]
        prefix_len += 1

min_steps = float('inf')
for i, c in enumerate(t):
    if trie_root.is_string_end:
        min_steps = min(min_steps, find_longest_prefix(text[i:], trie_root))

if min_steps == float('inf'):
    print(-1)
else:
    print(min_steps)
    for _ in range(min_steps):
        # find the longest prefix that is also a suffix of one of the strings s_i
        # and use it as the current step
        pass
