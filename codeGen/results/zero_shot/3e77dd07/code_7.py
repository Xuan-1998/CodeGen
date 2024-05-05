import sys

class Node:
    def __init__(self, char):
        self.char = char
        self.left = None
        self.right = None

def string_to_tree(s):
    if not s:
        return None

    node = Node(s[0])
    if len(s) == 1:
        return node

    mid = len(s) // 2
    node.left = string_to_tree(s[:mid])
    node.right = string_to_tree(s[mid:])
    return node

def tree_to_string(t):
    def traverse(node):
        if not node:
            return ""

        left_str = traverse(node.left)
        right_str = traverse(node.right)

        if left_str and right_str:
            return f"{left_str}{right_str}"
        elif left_str:
            return left_str
        else:
            return right_str

    return traverse(t).replace(" ", "")

def is_scrambled(t1, t2):
    def check_trees(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False

        node1 = t1
        node2 = t2

        while node1 and node2:
            if node1.char != node2.char:
                return False
            left_match = check_trees(node1.left, node2.left) and check_trees(node1.right, node2.right)
            right_match = check_trees(node1.left, node2.right) and check_trees(node1.right, node2.left)

            return left_match or right_match

        return False

    return check_trees(t1, t2)

def main():
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()

    t1 = string_to_tree(s1)
    t2 = string_to_tree(s2)

    result = is_scrambled(t1, t2)

    print(result)

if __name__ == "__main__":
    main()
