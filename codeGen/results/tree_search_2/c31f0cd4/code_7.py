def solve(nums):
    n = len(nums)
    max_sum = sum(nums)
    dp = [[set() for _ in range(n+1)] for _ in range(max_sum+1)]

    for i in range(1, n+1):  # generate all possible subsets
        for j in range(i, -1, -1):
            new_sum = sum(nums[j:i])
            if new_sum <= max_sum:
                dp[new_sum][i].add(new_sum)
    
    return ' '.join(map(str, sorted([sum(s) for s in dp])))
