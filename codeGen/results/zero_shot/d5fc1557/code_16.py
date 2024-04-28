n = int(input())
nums = list(map(int, input().split()))
max_length = 0
curr_length = 0
for num in nums:
    if num == 1:
        curr_length += 1
    else:
        max_length = max(max_length, curr_length)
        curr_length = 0
max_length = max(max_length, curr_length)
print(max_length)
