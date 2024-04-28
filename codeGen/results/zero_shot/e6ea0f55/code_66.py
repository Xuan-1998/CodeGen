n = int(input())
k = int(input())
nums = [int(x) for x in input().split()]
max_sum = float('-inf')
for i in range(n):
    max_sum = max(max_sum, sum(nums[i:i+k+1]))
print(max_sum)
