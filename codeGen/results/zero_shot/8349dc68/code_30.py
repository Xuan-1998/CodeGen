n = int(input())
arr = list(map(int, input().split()))
k = int(input())

ans = 0
max_sum = sum(arr)
i = 0
while i < n:
    if i + k > n:
        ans += max(arr[i:])
    else:
        sub_sum = sum(arr[i:i+k])
        ans += sub_sum
        i += k

print(ans)
