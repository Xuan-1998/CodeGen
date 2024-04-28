from bisect import bisect_left
n, k = map(int, input().split())
nums = list(map(int, input().split()))
max_sum = nums[0]
for i in range(n):
    index = bisect_left(nums[:i], min(max(0, i-k), max(0, i+k+1)))
    for j in range(index):
        max_sum = max(max_sum, sum(nums[j:i+1]))
print(max_sum)
