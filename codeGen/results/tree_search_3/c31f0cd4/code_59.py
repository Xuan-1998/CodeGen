def find_distinct_sums():
    n = int(input())
    nums = list(map(int, input().split()))
    
    dp = [[False] * (sum(nums) + 1) for _ in range(n + 1)]
    dp[0][0] = True
    
    for i in range(1, n + 1):
        for s in range(sum(nums) + 1):
            if nums[i - 1] <= s:
                dp[i][s] = dp[i - 1][s - nums[i - 1]] or dp[i - 1][s]
            else:
                dp[i][s] = dp[i - 1][s]
    
    distinct_sums = set()
    for s in range(1, sum(nums) + 1):
        if dp[n][s]:
            distinct_sums.add(s)
    
    return ' '.join(map(str, sorted(list(distinct_sums))))


print(find_distinct_sums())
