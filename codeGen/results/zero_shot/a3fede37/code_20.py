class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_sum_path(root):
    if root is None:
        return 0
    
    left_sum = max_sum_path(root.left)
    right_sum = max_sum_path(root.right)

    if root.left and root.right:
        return root.val + max(left_sum, right_sum)
    elif root.left:
        return root.val + left_sum
    elif root.right:
        return root.val + right_sum
    else:
        return root.val

def solve():
    n = int(input())
    tree = [None] * (n+1)
    
    for i in range(1, n+1):
        val = int(input())
        tree[i] = Node(val)

        left_child = 2*i + 1
        if left_child <= n:
            tree[i].left = tree[left_child]
        right_child = 2*i + 2
        if right_child <= n:
            tree[i].right = tree[right_child]

    print(max_sum_path(tree[1]))

if __name__ == "__main__":
    solve()
