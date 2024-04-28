n = int(input())
nums = [int(x) for x in input().split()]
ones_count = nums.count(1)
if ones_count == 0:
    print(0)
else:
    max_length = 0
    for i in range(n):
        if nums[i] == 1:
            current_length = 1
            for j in range(i+1, n):
                if nums[j] == 1:
                    current_length += 1
                else:
                    break
            max_length = max(max_length, current_length)
    print(max_length)
