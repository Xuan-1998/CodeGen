def max_sum_path_tree(tree):
    def helper(node, parent=None):
        if node == -1:  # special value indicating no child
            return 0
        
        left_sum = helper(2 * node + 1) if 2 * node + 1 < len(tree) else 0
        right_sum = helper(2 * node + 2) if 2 * node + 2 < len(tree) else 0

        max_sum = tree[node] + left_sum + right_sum
        return max_sum

    return max(helper(0), key=max)

if __name__ == "__main__":
    tree = [int(x) for x in input().split()]
    print(max_sum_path_tree(tree))
