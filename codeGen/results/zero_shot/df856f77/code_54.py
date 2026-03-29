code
n = int(input())
arr = list(map(int, input().split()))
min_ops = 0

for i in range(1, n):
    if arr[i] <= arr[i-1]:
        min_ops += arr[i-1] - arr[i] + 1

print(min_ops)
