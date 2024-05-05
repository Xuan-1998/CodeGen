import sys

n, m = map(int, input().split())
array = list(map(int, input().split()))
dp = [[False] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][i] = True
    if array[i - 1] <= array[i]:
        dp[i][i] = False

for len_subsegment in range(2, n + 1):
    for l in range(n - len_subsegment + 1):
        r = l + len_subsegment - 1
        prev = None
        min_val = array[l]
        max_val = array[r]
        for j in range(l, r + 1):
            if (prev is not None and array[j] < prev) or \
               (min_val > array[j]):
                dp[l][r] = False
                break
            min_val = min(min_val, array[j])
            max_val = max(max_val, array[j])
            prev = array[j]
        else:
            if len_subsegment == 2 and array[l] > array[r]:
                dp[l][r] = True
            else:
                dp[l][r] = True

for _ in range(m):
    l, r = map(int, input().split())
    print("Yes" if dp[l][r] else "No")
