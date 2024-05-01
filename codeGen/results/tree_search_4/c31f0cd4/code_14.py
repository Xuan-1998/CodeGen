import itertools

def find_distinct_sums(nums):
    max_sum = sum(nums)
    dp = {i: [[] for _ in range(max_sum + 1)] for i in range(len(nums) + 1)}
    
    # Populate the dp dictionary
    for i, num in enumerate(nums):
        for j in range(max_sum + 1):
            if j - num >= 0:
                dp[i][j].extend(dp[i-1][j-num] if j > num else [set([num])])
            elif not dp[i][j]:
                dp[i][j] = [set([num])]
    
    # Find the subsets that generate each distinct sum
    distinct_sums = set()
    for j in range(max_sum + 1):
        for subset in itertools.chain(*dp[-1][j]):
            if len(subset) > 0:
                distinct_sums.add(sum(subset))
    
    return ' '.join(map(str, sorted(list(distinct_sums))))


# Test your function
nums = list(map(int, input().split()))
print(find_distinct_sums(nums))
