code
def max_divisible_subset_sum(n, arr, m):
    dp = {0: True}
    total_sum = sum(arr)
    for i in range(total_sum // m + 1):
        dp[i] = False

    for num in arr:
        for j in range(i := total_sum - num, 0, -m):
            if not dp.get(j - num):
                dp[j] = True
    return any(dp.values())

n = int(input())
m = int(input())
arr = list(map(int, input().split()))
print(max_divisible_subset_sum(n, arr, m))
code

