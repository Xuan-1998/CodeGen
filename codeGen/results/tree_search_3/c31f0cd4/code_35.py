import sys

def generate_sums(nums):
    # Initialize memoization dictionary
    memo = {(0, 0): [0]}

    def recursive_generate_sums(cumulative_sum, current_index):
        if (cumulative_sum, current_index) in memo:
            return memo[(cumulative_sum, current_index)]

        sums = []
        for i in range(current_index + 1, len(nums)):
            new_cumulative_sum = cumulative_sum + nums[i]
            new_sums = recursive_generate_sums(new_cumulative_sum, i)
            sums.extend([new_cumulative_sum] + s for s in new_sums)

        memo[(cumulative_sum, current_index)] = sorted(list(set(sums)))
        return memo[(cumulative_sum, current_index)]

    # Main function to generate all distinct sums
    nums.sort()
    total_sum = sum(nums)
    distinct_sums = recursive_generate_sums(0, -1)

    # Print the result
    print(' '.join(map(str, distinct_sums)))

# Read input from stdin and process it
N = int(input())
nums = list(map(int, input().split()))
generate_sums(nums)
