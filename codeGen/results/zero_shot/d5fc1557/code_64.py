n = int(input())
nums = [int(x) for x in input().split()]
ones_count = 0
max_length = 0
for num in nums:
    if num == 1:
        ones_count += 1
        max_length = max(max_length, ones_count)
    else:
        ones_count = 0
print(max_length)
