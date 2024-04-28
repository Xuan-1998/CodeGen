n = int(input())
nums = [int(i) for i in input().split()]
max_len = 0
for i in range(len(nums)):
    if nums[i] == 1:
        max_len = max(max_len, 1)
        temp_max = 1
        for j in range(i+1, len(nums)):
            if nums[j] == 1:
                temp_max += 1
            else:
                break
        max_len = max(max_len, temp_max)

print(max_len)
