from itertools import combinations
k = int(input())
n = int(input())
nums = list(map(int, input().split()))
max_sum = 0
for r in range(1, n+1):
    for c in combinations(range(n), r):
        subseq_sum = sum([nums[i] for i in c])
        if all(abs(c[i]-c[i-1]) <= k for i in range(1, len(c))):
            max_sum = max(max_sum, subseq_sum)
print(max_sum)
