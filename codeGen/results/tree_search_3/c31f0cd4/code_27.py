from collections import defaultdict

def distinct_sums(nums):
    n = len(nums)
    dp = defaultdict(list)

    # Base cases: empty set and single-element set
    dp[0].append(0)  # sum of an empty set is 0

    for i in range(n):
        for prev_sum in list(dp.keys()):
            new_sums = [prev_sum + nums[i]]
            for j in range(i, -1, -1):
                if prev_sum == dp[prev_sum][j]:
                    new_sums.append(prev_sum + nums[i])
            dp[new_sums].extend([new_sum for new_sum in new_sums])

    return ' '.join(map(str, sorted(set(dp.keys()))))

# Example usage
N = int(input())
nums = list(map(int, input().split()))
print(distinct_sums(nums))
