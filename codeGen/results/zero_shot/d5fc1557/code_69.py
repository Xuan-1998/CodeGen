n = int(input())
nums = [int(x) for x in input().split()]
one_count = nums.count(1)
if one_count == 0:
    print(0)
else:
    max_length = 0
    one_start = -1
    one_end = -1
    ones = 0
    for i in range(n):
        if nums[i] == 1:
            ones += 1
            if ones > 1 and (one_start == -1 or i - one_start > max_length):
                max_length = i - one_start
            if ones > 1 and i - one_end > max_length:
                max_length = i - one_end
        else:
            ones = 0
            one_start = i
            one_end = i
    print(max_length)
