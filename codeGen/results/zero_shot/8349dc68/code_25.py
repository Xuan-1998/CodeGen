n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(max(max(subarray) for subarray in [arr[i:i+k] for i in range(0, n-k+1)]))
