n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
max_val = max(arr)
if max_val > k:
    count += 1
print(count)
