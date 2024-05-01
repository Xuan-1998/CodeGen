import sys

class SuffixTree:
    def __init__(self, s):
        self.root = {}
        for i in range(len(s)):
            self._build_tree(s[i:], i)

    def _build_tree(self, s, start):
        if not s:
            return
        node = self.root
        for c in s:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['$'] = start

    def query(self, s):
        node = self.root
        for c in s:
            if c not in node:
                return None
            node = node[c]
        if '$' in node:
            return node['$']
        return None

def find_common_substrings(str1, str2):
    tree1 = SuffixTree(str1)
    tree2 = SuffixTree(str2)

    max_count = 0
    for i in range(len(str1)):
        for j in range(i + 1, len(str1) + 1):
            substring = str1[i:j]
            if tree2.query(substring):
                max_count += 1

    return max_count

def main():
    str1 = input().strip()
    str2 = input().strip()

    print(find_common_substrings(str1, str2))

if __name__ == "__main__":
    main()
