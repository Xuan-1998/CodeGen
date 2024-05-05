def read_tree():
    n = int(input())
    tree = list(map(int, input().split()))
    
    return tree

def max_sum_of_path(tree):
    if not tree or tree[0] < 0:
        return 0
    
    left_sum = max_sum_of_path(tree[1:2] + [tree[0] // 2]) if len(tree) > 1 else 0
    right_sum = max_sum_of_path(tree[3:] + [tree[0] % 2]) if len(tree) > 3 else 0
    
    return tree[0] + max(left_sum, right_sum)

tree = read_tree()
print(max_sum_of_path(tree))
