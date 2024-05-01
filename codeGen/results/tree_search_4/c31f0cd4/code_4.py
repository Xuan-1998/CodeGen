def find_distinct_sums(nums):
    seen = set()
    result = set()

    def dfs(index, total_sum):
        if index >= len(nums):
            return

        for i in range(index, len(nums)):
            new_total_sum = total_sum + nums[i]
            if new_total_sum not in seen:
                seen.add(new_total_sum)
                result.add(new_total_sum)
                dfs(i+1, new_total_sum)

    dfs(0, 0)
    return sorted(list(result))

# test the function
nums = [int(x) for x in input().split()]
print(" ".join(map(str, find_distinct_sums(nums))))
