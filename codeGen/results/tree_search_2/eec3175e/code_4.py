from collections import defaultdict

def can_sum_divisible_by_m(arr, m):
    n = len(arr)
    dp = [False] * (n + 1)
    dp[0] = True
    mod_values = defaultdict(int)

    for i in range(n):
        for j in range(i+1, -1, -1):
            if arr[j-1] % m == 0:
                mod_values[arr[j-1]%m] += 1

        for k in mod_values:
            if (k*m)%m==0 and dp[k]:
                dp[i+1] = True
                break
        else:
            continue
        break

    return dp[-1]

n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(can_sum_divisible_by_m(arr, m))
