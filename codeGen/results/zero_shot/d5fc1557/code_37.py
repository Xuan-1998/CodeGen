n = int(input())
nums = list(map(int, input().split()))
ones_count = nums.count(1)
if ones_count == 0:
    print(0)
else:
    max_length = 0
    for i in range(n):
        if nums[i] == 1:
            start = i
            while i < n - 1 and nums[i + 1] == 1:
                i += 1
            max_length = max(max_length, i - start + 1)
    print(max_length)
