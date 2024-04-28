n = int(input())
nums = [int(x) for x in input().split()]
max_length = 0
current_length = 0
for i in range(n):
    if nums[i] == 1:
        current_length += 1
        max_length = max(max_length, current_length)
    else:
        current_length = 0
print(max_length)
