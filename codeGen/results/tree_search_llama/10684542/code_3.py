class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def get_exponent(n, p):
    root = Node(1)
    for i in range(2, int(math.log2(n)) + 1):
        if n >= p ** i:
            node = Node(p ** i)
            if root.val < node.val:
                root.right = node
            else:
                temp = root
                while temp.right and temp.right.val < node.val:
                    temp = temp.right
                temp.right = node
        else:
            break

    def find_exponent(node, n):
        if node.val > n:
            return 0
        elif node.val == n:
            return node.val.bit_length() - 1
        else:
            return 1 + find_exponent(node.right, n - node.val)

    return find_exponent(root, n)
