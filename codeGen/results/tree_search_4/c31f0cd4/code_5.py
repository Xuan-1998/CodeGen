def find_distinct_sums():
    N = int(input())
    nums = list(map(int, input().split()))
    
    dp = [[0] * (N+1) for _ in range(sum(nums)+1)]
    for j in range(N+1):
        dp[0][j] = 1
    
    for i in range(1, sum(nums)+1):
        ways = [0] * (N+1)
        for j in reversed(range(N)):
            if i - nums[j] >= 0:
                ways[j] += dp[i-nums[j]][j]
        dp[i][0] = sum(ways)
    
    distinct_sums = set()
    for i in range(sum(nums)+1):
        if dp[sum(nums)][i]:
            distinct_sums.add(i)
    
    print(' '.join(map(str, sorted(list(distinct_sums)))))


if __name__ == "__main__":
    find_distinct_sums()

