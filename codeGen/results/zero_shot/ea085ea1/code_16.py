import collections

class SuffixTree:
    def __init__(self, s):
        self.s = s
        self.tree = {}
        self.build_tree()

    def build_tree(self):
        for i in range(len(self.s)):
            self.insert_suffix(i)

    def insert_suffix(self, start):
        node = self.tree
        for j in range(start, len(self.s)):
            c = self.s[j]
            if c not in node:
                node[c] = {}
            node = node[c]
            if '$' not in node:
                node['$'] = []
                node['$'].append((start, j))

    def get_suffixes(self):
        for i in range(len(self.s)):
            self.insert_suffix(i)
        return self.tree.get('$', [])

def find_common_substrings(str1, str2):
    suffix_tree1 = SuffixTree(str1 + '$')
    suffix_tree2 = SuffixTree(str2 + '$')

    common_substrings = set()
    for start, end in suffix_tree1.get_suffixes():
        if (start, end) in suffix_tree2.get_suffixes():
            common_substrings.add((start, end))

    return len(common_substrings)

def main():
    str1 = input()
    str2 = input()

    max_common_substrings = find_common_substrings(str1, str2)
    print(max_common_substrings)

if __name__ == "__main__":
    main()
