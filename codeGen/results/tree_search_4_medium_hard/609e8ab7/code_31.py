def min_operations(n, parent, ranges):
    memo = {}

    def dp(i):
        if i not in memo:
            if i == n:  # base case: no more vertices to process
                memo[i] = 0
            else:
                start, end = ranges[i]
                diff = end - start

                # consider adding values to ancestors on the path to the root
                for j in range(i + 1, parent[i] + 1):
                    memo[j].get()  # get the minimum number of operations needed for ancestors

                # calculate the minimum number of operations needed for this vertex
                min_ops = max(0, diff)  # at least one operation is needed if the range isn't already within
                if parent[i] > 0:  # consider adding values to parents on the path to the root
                    memo[parent[i]].get()  # get the minimum number of operations needed for the parent
                    min_ops = max(min_ops, dp(parent[i]) + (end - start))

                memo[i] = min_ops

        return memo[i]

    total_ops = 0
    for i in range(1, n + 1):
        total_ops += dp(i)

    print(total_ops)
