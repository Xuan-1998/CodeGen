arr = list(map(int, input().split()))
k = int(input())
ans = 0
max_val = max(arr)
for i in range(0, len(arr), k):
    ans += min(k, len(arr) - i) * max_val
print(ans)
