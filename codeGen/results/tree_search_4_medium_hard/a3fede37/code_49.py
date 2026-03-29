def max_path_sum(tree):
    n = len(tree)
    memo = {i: tree[i] for i in range(n)}

    def helper(i):
        if i < 0:
            return -float('inf')
        elif i not in memo:
            left_sum = helper(2*i+1) if 2*i+1 < n else -float('inf')
            right_sum = helper(2*i+2) if 2*i+2 < n else -float('inf')
            memo[i] = max(left_sum, right_sum) + tree[i]
        return memo[i]

    return max(helper(i) for i in range(n))
