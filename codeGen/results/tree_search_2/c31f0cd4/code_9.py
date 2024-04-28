def subset_sums(nums):
    memo = {}
    total_sums = set()

    def dp(current_sum, remaining_elements):
        if (current_sum, tuple(remaining_elements)) in memo:
            return memo[(current_sum, tuple(remaining_elements))]
        
        result = {current_sum}
        
        for i, num in enumerate(remaining_elements):
            new_remaining = remaining_elements[:i] + remaining_elements[i+1:]
            for subset_sum in dp(current_sum + num, new_remaining):
                result.add(subset_sum)
        
        memo[(current_sum, tuple(remaining_elements))] = result
        return result

    def generate_sums(nums):
        for i in range(len(nums)):
            for mask in range(2**len(nums[i+1:])):
                subset = [num for j, num in enumerate(nums[i+1:]) if (mask >> j) & 1]
                yield current_sum + sum(subset)

    total_sum = sum(nums)
    dp(total_sum, nums)

    sums = set()
    for current_sum in range(0, total_sum+1):
        if current_sum not in memo[0]:
            continue
        for remaining_elements in [tuple(nums[i+1:]) for i in range(len(nums))]:
            for subset_sum in memo[current_sum]:
                if any(num > subset_sum for num in nums[:i]):
                    break
            else:
                sums.add(subset_sum)

    return ' '.join(map(str, sorted(sums)))

import sys

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    print(subset_sums(nums))
