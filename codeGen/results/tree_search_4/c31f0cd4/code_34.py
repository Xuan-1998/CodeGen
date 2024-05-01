from collections import defaultdict

def generate_distinct_sums(nums):
    n = len(nums)
    total_sum = sum(nums)
    
    # Initialize dp table with zeros
    dp = defaultdict(int)
    dp[0] = 1
    
    for num in nums:
        new_dp = defaultdict(int)
        for j, count in dp.items():
            new_j = j + num
            if new_j <= total_sum:
                new_dp[new_j] += count
            new_dp[j] += count
        dp = new_dp
    
    # Find distinct sums and print them out
    distinct_sums = [j for j in range(total_sum + 1) if dp[j]]
    print(' '.join(map(str, sorted(distinct_sums))))

# Read input from stdin
n = int(input())
nums = list(map(int, input().split()))

generate_distinct_sums(nums)
