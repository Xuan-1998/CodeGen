n = int(input())
nums = [int(x) for x in input().split()]
max_length = 0
cur_length = 0

for num in nums:
    if num == 1:
        cur_length += 1
        max_length = max(max_length, cur_length)
    else:
        cur_length = 0

print(max_length - (1 if n > max_length else 0))
