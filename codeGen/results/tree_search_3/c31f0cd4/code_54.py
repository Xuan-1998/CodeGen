def subset_sums(nums):
    nums.sort()
    unique_sums = set()

    def backtrack(start, current_sum):
        if start == len(nums):
            unique_sums.add(current_sum)
            return
        backtrack(start + 1, current_sum)
        backtrack(start + 1, current_sum + nums[start])

    backtrack(0, 0)
    return sorted(list(unique_sums))

N = int(input())
nums = [int(x) for x in input().split()]
print(' '.join(map(str, subset_sums(nums))))
