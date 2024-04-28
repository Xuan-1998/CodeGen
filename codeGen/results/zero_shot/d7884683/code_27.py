n = int(input())
arr = list(map(int, input().split()))
left_sum = sum(arr[:n//2])
right_sum = left_sum
ans = 1
for i in range(n//2+1, n):
    if arr[i] == abs(left_sum - right_sum):
        ans += 1
        left_sum = sum(arr[:i])
        right_sum = left_sum
print(ans)
