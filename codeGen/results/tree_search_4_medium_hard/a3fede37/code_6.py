def max_path_sum(tree):
    memo = {}

    def helper(i):
        if i < 0:
            return -1001
        if i >= len(tree):
            return -1001
        if (i, ) in memo:
            return memo[(i,)]

        left_sum = helper(2 * i + 1)
        right_sum = helper(2 * i + 2)

        node_val = tree[i]
        max_sum = node_val
        if left_sum > -1000 and right_sum > -1000:
            max_sum = node_val + min(left_sum, right_sum)
        memo[(i,) ]=max_sum

        return max_sum

    return helper(0)
