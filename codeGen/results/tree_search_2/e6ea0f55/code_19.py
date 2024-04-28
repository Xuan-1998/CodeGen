import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())

result = maxSumSubsequence(nums, k)
print(result)
