n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(len(arr)):
    for j in range(i+1, len(arr)+1):
        if max(arr[i:j]) > k:
            ans += 1
print(ans)
