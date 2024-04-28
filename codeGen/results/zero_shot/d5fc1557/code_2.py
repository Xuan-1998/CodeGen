n = int(input())
nums = list(map(int, input().split()))
max_length = 0
curr_length = 0
for i in range(n):
    if nums[i] == 1:
        curr_length += 1
        max_length = max(max_length, curr_length)
    else:
        curr_length = 0
print(max_length)
