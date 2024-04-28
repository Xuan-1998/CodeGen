def subset_sum_sums(nums):
    def dfs(i, total):
        if total not in memo:
            memo[total] = []
        for j in range(i, len(nums)):
            memo[total].append(dfs(j+1, total+nums[j]))
        return memo[total]

    memo = {}
    sums = set()
    for i in range(len(nums)):
        dfs(i, 0)
    return ' '.join(map(str, sorted(list(sums))))

n = int(input())
nums = list(map(int, input().split()))
print(subset_sum_sums(nums))
