n = int(input())
nums = [int(i) for i in input().split()]
count_ones = 0
max_length = 0
current_length = 0
for num in nums:
    if num == 1:
        current_length += 1
        count_ones += 1
        max_length = max(max_length, current_length)
    else:
        current_length = 0
print(max(0, count_ones - 1))
