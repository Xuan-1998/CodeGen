from collections import defaultdict

def all_distinct_sums(a):
    n = len(a)
    dp = [[set()] for _ in range(n + 1)]
    memo = {}

    def dfs(i, current_sum):
        if (i, current_sum) in memo:
            return memo[(i, current_sum)]
        if i == 0:
            return {current_sum}

        sums = set()
        for j in range(i + 1):
            for s in dfs(j, current_sum - a[j]):
                sums.add(current_sum)
                sums.update(s)
        memo[(i, current_sum)] = sums
        return sums

    result = set()
    for i in range(n + 1):
        result.update(dfs(i, 0))

    return ' '.join(map(str, sorted(result)))
