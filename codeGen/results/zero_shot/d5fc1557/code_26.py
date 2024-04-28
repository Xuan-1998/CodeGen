n = int(input())
nums = [int(x) for x in input().split()]
if all(i == 1 for i in nums):
    print(len(nums))
else:
    max_len = 0
    curr_len = 0
    for i in range(n):
        if nums[i] == 1:
            curr_len += 1
        else:
            max_len = max(max_len, curr_len)
            curr_len = 0
    print(max(max_len, curr_len))
