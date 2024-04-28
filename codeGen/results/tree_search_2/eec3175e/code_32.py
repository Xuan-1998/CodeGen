code
n, m = map(int, input().split())
arr = list(map(int, input().split()))
cum_sums = [0] * (n + 1)
for i in range(n):
    cum_sums[i + 1] = cum_sums[i] + arr[i]

ans = any(cum_sum % m == 0 for cum_sum in cum_sums)
print(1 if ans else 0)
