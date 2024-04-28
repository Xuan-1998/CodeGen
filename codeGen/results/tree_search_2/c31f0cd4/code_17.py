from collections import defaultdict

def find_distinct_sums():
    n = int(input())
    nums = list(map(int, input().split()))
    
    dp = defaultdict(set)
    dp[0][0] = {0}
    
    for i in range(1, n + 1):
        for j in range(max(dp[i-1].keys()) + 1):
            if j > 0:
                for subset_sum in list(dp[i-1][j]):
                    new_sum = j + nums[i - 1]
                    dp[i][new_sum] |= {subset_sum + nums[i - 1]}
    
    sums = sorted({sum}.union(*dp.values()))
    print(' '.join(map(str, sums)))

find_distinct_sums()
