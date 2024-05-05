import sys

n, m = map(int, input().split())
array = list(map(int, input().split()))
dp = [False] * (n + 1)

def longest_non_decreasing_subsequence(i):
    if dp[i]:
        return i
    result = 0
    for j in range(i):
        if array[j] <= array[i]:
            result = max(result, longest_non_decreasing_subsequence(j))
            break
    dp[i] = True
    return result

for _ in range(m):
    l, r = map(int, input().split())
    if array[l-1] > array[r-1]:
        print("No")
    else:
        i = max(longest_non_decreasing_subsequence(l-1), longest_non_decreasing_subsequence(r))
        for j in range(i+1, n):
            if array[i] <= array[j]:
                i = j
                break
        if i < r:
            print("Yes")
        else:
            print("No")
