n = int(input())
nums = [int(x) for x in input().split()]
one_count = nums.count(1)
if one_count == 0:
    print(0)
else:
    print(max(sum(1 for num in nums[:i] + nums[i+1:]) for i in range(n-1)) if n > 1 else 0)
