n = int(input())
nums = [int(i) for i in input().split()]
ones_count = nums.count(1)
max_length = 0
for i in range(n):
    if nums[i] == 1:
        ones_count -= 1
        max_length = max(max_length, ones_count + 1)
    else:
        ones_count = 0
print(max_length)
