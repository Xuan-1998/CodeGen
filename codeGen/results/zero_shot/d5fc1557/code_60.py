n = int(input())
nums = list(map(int, input().split()))
count_ones = 0
max_length = 0
for i in range(n):
    if nums[i] == 1:
        count_ones += 1
        max_length = max(max_length, count_ones)
    else:
        count_ones = 0

print(max_length)
