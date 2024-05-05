class Node:
    def __init__(self, char, left=None, right=None):
        self.char = char
        self.left = left
        self.right = right

def build_tree(s):
    if not s:
        return None
    mid = len(s) // 2
    return Node(s[:mid], build_tree(s[:mid]), build_tree(s[mid:]))

def is_scrambled(s1, s2):
    def dfs(t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        if t1.char != t2.char:
            return False
        return (dfs(t1.left, t2.right) and dfs(t1.right, t2.left))

    tree1 = build_tree(s1)
    tree2 = build_tree(s2)
    return dfs(tree1, tree2)

def main():
    s1 = input()
    s2 = input()
    print(is_scrambled(s1, s2))

if __name__ == "__main__":
    main()
