from itertools import combinations
n, k = [int(i) for i in input().split()]
nums = [int(i) for i in input().split()]
max_sum = 0
for r in range(1, len(nums)):
    for subseq in combinations(enumerate(nums), r):
        if all(abs(subseq[i][1] - subseq[i-1][1]) <= k for i in range(1, len(subseq))):
            max_sum = max(max_sum, sum(num for _, num in subseq))
print(max_sum)
