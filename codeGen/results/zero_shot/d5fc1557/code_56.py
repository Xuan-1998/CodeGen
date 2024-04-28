n = int(input())
nums = [int(x) for x in input().split()]
one_count = nums.count(1)
if one_count > 0:
    max_length = 0
    current_length = 0
    for num in nums:
        if num == 1:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0
    print(max_length)
else:
    print(0)
