n = int(input())
k = int(input())
nums = list(map(int, input().split()))
max_sum = float('-inf')
left = 0
for right in range(len(nums)):
    while nums[right] - nums[left] > k:
        left += 1
    max_sum = max(max_sum, sum(nums[i] for i in range(left, right+1)))
