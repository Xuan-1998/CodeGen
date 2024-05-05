from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end_of_string = False

def build_trie(strings):
    root = TrieNode()
    for string in strings:
        node = root
        for char in string:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_string = True
    return root

def find_occurrences(text):
    result = []
    node = trie_root
    for char in text:
        if char not in node.children:
            break
        node = node.children[char]
        if node.is_end_of_string:
            result.append((node, char))
    return result

def calculate_min_steps(occurrences):
    max_length = 0
    for occurrence in occurrences:
        length = len(list(occurrence[1]))
        if length > max_length:
            max_length = length
    return max_length

t = input()
n = int(input())
strings = []
for _ in range(n):
    strings.append(input())

trie_root = build_trie(strings)
occurrences = find_occurrences(t)
min_steps = calculate_min_steps(occurrences)

print(min_steps)

for i, (node, char) in enumerate(occurrences):
    print(f"{i+1} {char}")
