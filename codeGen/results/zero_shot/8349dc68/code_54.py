n = int(input())
arr = list(map(int, input().split()))
k = int(input())

ans = 0
cur_sum = max_val = sum(arr[:k])
for i in range(k, n):
    cur_sum = cur_sum + arr[i] - max(arr[:k])
    ans = max(ans, cur_sum)
print(ans)
