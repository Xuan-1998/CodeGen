def max_path_sum(root):
    if root is None:
        return 0

    left_sum = max_path_sum(root[1])
    right_sum = max_path_sum(root[2])

    current_sum = root + max(left_sum, right_sum)

    return current_sum

def read_input():
    n = int(input())
    tree = []
    for _ in range(n):
        node = list(map(int, input().split()))
        tree.append(node)
    return tree

if __name__ == "__main__":
    tree = read_input()
    root_idx = 0
    max_sum = max_path_sum(tree[root_idx])
    print(max_sum)
