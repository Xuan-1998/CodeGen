def find_distinct_sums(nums):
    n = len(nums)
    max_sum = sum(nums)
    dp = {0: 1}
    
    for num in nums:
        temp = {}
        for total in sorted(dp.keys()):
            temp[total + num] = temp.get(total + num, 0) + dp[total]
        dp.update(temp)
    
    return [sum for sum in range(max_sum+1) if sum in dp]

# Example usage
N = int(input())
nums = list(map(int, input().split()))
print(" ".join(map(str, find_distinct_sums(nums))))
