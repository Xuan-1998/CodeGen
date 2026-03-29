import sys

def read_input():
    n = int(input())
    arr = [int(x) for x in input().split()]
    return n, arr

def LIS_length(a, dp):
    if a == -1:
        return 0
    max_length = 0
    for i in range(len(dp)):
        if dp[i] > a and (i == len(dp) - 1 or dp[i + 1] <= a):
            max_length = max(max_length, LIS_length(i, dp) + 1)
    return max_length

def solve():
    n, arr = read_input()
    dp = [-1] * n
    for i in range(n):
        j = i - 1
        while j >= 0 and arr[i] > arr[j]:
            j -= 1
        dp[i] = i if j == -1 else j + 1
    print(max(LIS_length(i, dp) for i in range(n)))

if __name__ == "__main__":
    solve()
