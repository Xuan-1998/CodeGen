n = int(input())
arr = list(map(int, input().split()))
k = int(input())

res = sum(max(arr[i:i+k]) for i in range(0, n, k))
print(res)
