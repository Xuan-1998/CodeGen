def subset_sums(a):
    n = len(a)
    dp = {(0, i): 0 for i in range(n)} | {(1, i): a[i] for i in range(n)}
    target_sum = sum(a)

    def dfs(i, target_sum):
        if target_sum == 0:
            return [0]
        if target_sum < 0 or (target_sum, i) in dp and dp[(target_sum, i)] != float('inf'):
            return []
        result = []
        for j in range(i + 1, n):
            new_target_sum = target_sum - a[j]
            subsets = dfs(j, new_target_sum)
            if new_target_sum >= 0:
                for subset in subsets:
                    result.append(a[i] + subset)
        dp[(target_sum, i)] = result if len(result) > 0 else float('inf')
        return result

    result = set()
    for i in range(n):
        for target_sum in range(1, target_sum + 2):
            subsets = dfs(i, target_sum - a[i])
            if len(subsets) > 0:
                result.update({a[i] + s for s in subsets})

    return ' '.join(map(str, sorted(result)))
