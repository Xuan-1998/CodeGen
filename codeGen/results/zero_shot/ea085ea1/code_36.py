import sys

class SuffixTree:
    def __init__(self, string):
        self.root = {}
        self.build(string)

    def build(self, string):
        for i in range(len(string)):
            suffix = string[i:]
            node = self.root
            for char in suffix:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['$'] = None

    def search(self, pattern):
        node = self.root
        for char in pattern:
            if char not in node:
                return False
            node = node[char]
            if '$' in node:
                return True
        return False

def find_common_substrings(str1, str2):
    N = len(str1)
    suffix_tree1 = SuffixTree(str1 + '#' + str2)  # Add the second string as a suffix to the first string
    common_substrings = 0
    for i in range(N):
        for j in range(i+1, N+1):  # Iterate through all possible substrings of the first string
            if suffix_tree1.search(str1[i:j]):  # Check if the substring is a prefix of the second string
                common_substrings += 1
    return common_substrings

# Read input from stdin
str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

# Print the output to stdout
print(find_common_substrings(str1, str2))
