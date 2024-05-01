from collections import defaultdict

def subsetSums(nums):
    N = len(nums)
    dp = defaultdict(set)

    for i in range(N+1):
        for j in range(i+1):
            if j == 0:
                dp[i].add(0)
            else:
                for prev_sum in dp[j-1]:
                    dp[i].add(prev_sum + nums[i-1])
    return sorted(list(dp[N]))

# Read input
N = int(input())
nums = list(map(int, input().split()))

print(' '.join(map(str, subsetSums(nums))))
