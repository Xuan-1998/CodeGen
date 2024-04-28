n = int(input())
arr = list(map(int, input().split()))
k = int(input())

max_sum = float('-inf')
for i in range(0, n, k):
    subarray = arr[i:i+k]
    max_sum = max(max_sum, sum(subarray))
print(max_sum)
