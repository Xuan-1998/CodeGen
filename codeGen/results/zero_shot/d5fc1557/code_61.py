n = int(input())
nums = [int(x) for x in input().split()]
if sum(nums) == 0:
    print(0)
else:
    one_count = 0
    max_length = 0
    for num in nums:
        if num == 1:
            one_count += 1
        else:
            max_length = max(max_length, one_count)
            one_count = 0
    max_length = max(max_length, one_count)
    print(n - 1)
