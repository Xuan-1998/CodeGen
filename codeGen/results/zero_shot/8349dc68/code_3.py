n = int(input())
arr = list(map(int, input().split()))
k = int(input())

ans = 0
sum_val = [0] * (n + 1)
for i in range(n):
    sum_val[i + 1] = sum_val[i] + arr[i]

max_sum = float('-inf')
for i in range(k, n + 1):
    max_sum = max(max_sum, sum_val[i] - sum_val[i - k])

print(max_sum)
