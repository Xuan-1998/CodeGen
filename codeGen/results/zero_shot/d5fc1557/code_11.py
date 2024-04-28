n = int(input())
nums = [int(x) for x in input().split()]
ones = 0
max_ones = 0
for i in range(n):
    if nums[i] == 1:
        ones += 1
        max_ones = max(max_ones, ones)
    else:
        ones = 0

print(max_ones)
