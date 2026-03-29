import sys

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n  # Initialize DP array with ones, since a single element is always an increasing subsequence of length 1

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)  # Return the maximum length found


def main():
    arr = list(map(int, input().split()))
    print(longest_increasing_subsequence(arr))


if __name__ == "__main__":
    main()
