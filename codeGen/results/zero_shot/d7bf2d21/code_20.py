import sys

def count_lis(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)  # Count the number of longest increasing subsequences

if __name__ == "__main__":
    input_line = sys.stdin.readline().strip()
    arr = [int(x) for x in input_line.split()]
    print(count_lis(arr))
