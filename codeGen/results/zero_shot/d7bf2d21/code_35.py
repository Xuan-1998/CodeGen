import sys

def lis_length(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def count_lis_length(arr):
    n = len(arr)
    lis_lengths = [0] * (n + 1)

    for i in range(n):
        j = i
        while j >= 0 and arr[i] > arr[j]:
            j -= 1
        if j < 0:
            continue
        length = i - j
        if length == lis_lengths[length]:
            lis_lengths[length] += 1
        else:
            break

    return lis_lengths[-1]


arr = list(map(int, input().split()))
print(count_lis_length(arr))
