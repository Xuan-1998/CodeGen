import sys

def read_input():
    return [int(x) for x in input().split()]

def lis(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

def solve():
    arr = read_input()
    print(lis(arr))

if __name__ == "__main__":
    solve()
