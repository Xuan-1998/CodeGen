T = int(stdin.readline())
for _ in range(T):
    n, p_dict, l_range = read_tree(stdin)
    ops = min_ops(n, p_dict, l_range)
    print(ops)
