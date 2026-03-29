import sys

def is_scrambled(s1, s2):
    def construct_tree(s):
        if len(s) == 0:
            return None
        mid = len(s) // 2
        left = construct_tree(s[:mid])
        right = construct_tree(s[mid:])
        return TreeNode(left, s[mid], right)

    class TreeNode:
        def __init__(self, left, val, right):
            self.left = left
            self.val = val
            self.right = right

    tree1 = construct_tree(s1)
    tree2 = construct_tree(s2)

    def in_order_traversal(tree):
        if tree is None:
            return ""
        return in_order_traversal(tree.left) + str(tree.val) + in_order_traversal(tree.right)

    in_order_s1 = in_order_traversal(tree1)
    in_order_s2 = in_order_traversal(tree2)

    return in_order_s1 == in_order_s2

def main():
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    print(is_scrambled(s1, s2))

if __name__ == "__main__":
    main()
