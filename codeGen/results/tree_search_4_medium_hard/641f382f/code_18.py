from math import gcd
from sys import stdin

def compute_gcd_subarrays(arr, n):
    gcd_subarrays = [[0] * n for _ in range(n)]
    for i in range(n):
        gcd_subarrays[i][i] = arr[i]
        for j in range(i + 1, n):
            gcd_subarrays[i][j] = gcd(gcd_subarrays[i][j - 1], arr[j])
    return gcd_subarrays

def min_operations_to_make_ones(arr, n, gcd_subarrays):
    if all(x == 1 for x in arr):
        return 0

    if gcd_subarrays[0][n - 1] != 1:
        return -1

    dp = [[[float('inf')] * 2 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        if arr[i] == 1:
            dp[i][i][1] = 0
        else:
            dp[i][i][0] = 0

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                if gcd_subarrays[i][j] == 1:
                    dp[i][j][1] = min(dp[i][j][1], dp[i][k][1] + dp[k + 1][j][1] + 1)

    return dp[0][n - 1][1] if dp[0][n - 1][1] != float('inf') else -1

def main():
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split()))

    gcd_subarrays = compute_gcd_subarrays(arr, n)
    result = min_operations_to_make_ones(arr, n, gcd_subarrays)
    print(result)

if __name__ == "__main__":
    main()
