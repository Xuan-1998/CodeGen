n = int(input())
arr = list(map(int, input().split()))
k = int(input())

max_sum = 0
for i in range(0, n, k):
    subarray = arr[i:i+k]
    max_sum += max(subarray)

print(max_sum)
