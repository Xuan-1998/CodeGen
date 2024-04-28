n = int(input())
k = int(input())
nums = [int(x) for x in input().split()]
max_sum = max_diff = 0
for i in range(len(nums)):
    for j in range(i+1, min(i+k+1, len(nums))):
        curr_sum = sum(nums[i:j+1])
        if curr_sum > max_sum:
            max_sum = curr_sum
        if abs(j-i) > k:
            break
print(max_sum)
