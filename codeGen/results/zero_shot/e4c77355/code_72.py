import sys

def read_input():
    return [int(x) for x in input().split()]

def longest_increasing_subsequence(arr):
    n = len(arr)
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    return max(lis)

arr = read_input()
print(longest_increasing_subsequence(arr))
