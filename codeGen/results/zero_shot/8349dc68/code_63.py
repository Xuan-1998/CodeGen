n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(max(sum(arr[i:i+k]) for i in range(0, n, k)))
