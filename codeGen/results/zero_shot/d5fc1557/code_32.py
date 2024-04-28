n = int(input())
nums = [int(x) for x in input().split()]
one_count = nums.count(1)
max_length = 0
curr_length = 0
for i in range(n):
    if nums[i] == 1:
        curr_length += 1
        max_length = max(max_length, curr_length)
    else:
        curr_length = 0

print(max_length - (one_count - 1) + (1 if one_count > 0 else 0))
