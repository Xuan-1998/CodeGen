nums = [int(x) for x in input().split()]
k = int(input())
max_sum = float('-inf')
for i in range(len(nums)):
    window_sum = 0
    for j in range(i, len(nums)):
        if j - i <= k:
            window_sum += nums[j]
        else:
            break
    max_sum = max(max_sum, window_sum)
print(max_sum)
