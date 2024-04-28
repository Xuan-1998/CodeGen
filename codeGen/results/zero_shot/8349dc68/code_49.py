n, k = map(int, input().split())
arr = list(map(int, input().split()))
max_sum = 0
for i in range(0, n, k):
    subarray = arr[i:i+k]
    max_sum += max(subarray)
print(max_sum)
