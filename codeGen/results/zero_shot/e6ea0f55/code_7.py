from itertools import combinations

n = int(input())
k = int(input())
nums = [int(x) for x in input().split()]

max_sum = float('-inf')

for i in range(1, len(nums)):
    for j in range(i):
        if nums[j] <= nums[i]:
            diff = i - j
            if diff > k:
                break
            subseq_sum = sum([nums[x] for x in list(combinations(range(j, i+1), 2))])
            max_sum = max(max_sum, subseq_sum)

print(max_sum)
