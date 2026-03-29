import sys

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_string = False

def build_trie(strings):
    root = TrieNode()
    for string in strings:
        node = root
        for char in string:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_string = True
    return root

def min_steps(t, strings):
    trie = build_trie(strings)
    steps = 0
    for char in t:
        found = False
        node = trie
        while True:
            if node.is_string:
                found = True
                break
            for child in node.children.values():
                if child.is_string or (child.is_string == False and char in child.children):
                    node = child
                    break
            else:
                node = None
                break
        if not found:
            steps += 1
    return steps

def output_solution(t, strings, steps):
    m = steps
    for j in range(m):
        w_j = ...  # find the index of the string used
        p_j = ...  # find the starting position of the string used
        print(f"{w_j} {p_j}")

t = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
strings = []
for _ in range(n):
    strings.append(sys.stdin.readline().strip())

output_solution(t, strings, min_steps(t, strings))
