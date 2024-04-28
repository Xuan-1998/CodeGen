n = int(input())
nums = [int(x) for x in input().split()]
count = 0
max_count = 0
for i in range(n):
    if nums[i] == 1:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0
print(max(max_count, n - count))
