===BEGIN CODE===
def longest_increasing_subsequence():
    n = int(input())
    L = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                L[i] = max(L[i], L[j] + 1)

    return max(L)

arr = list(map(int, input().split()))
print(longest_increasing_subsequence())
===END CODE===
