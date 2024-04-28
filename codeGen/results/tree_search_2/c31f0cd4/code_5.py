def distinct_sums(set):
    n = len(set)
    memo = {}

    def dfs(subset_sum, current_index):
        if (subset_sum, current_index) in memo:
            return memo[(subset_sum, current_index)]

        if subset_sum == 0 or current_index >= n:
            return [0]  # base case: only one sum (0)

        sums = []
        for i in range(current_index, n):
            sums.extend(dfs(subset_sum + set[i], i))
        memo[(subset_sum, current_index)] = sorted(list(set(sums)))
        return memo[(subset_sum, current_index)]

    all_sums = set()
    for i in range(n):
        all_sums.update(dfs(0, i))
    return ' '.join(map(str, all_sums))

n = int(input())
set = list(map(int, input().split()))
print(distinct_sums(set))
