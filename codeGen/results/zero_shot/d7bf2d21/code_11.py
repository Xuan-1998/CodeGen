import sys

def count_longest_increasing_subsequences(arr):
    n = len(arr)
    dp = [1] * n  # Initialize longest increasing subsequence length for each element

    max_length = 0
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        max_length = max(max_length, dp[i])

    count = 0
    for length in dp:
        if length == max_length:
            count += 1

    return count


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_longest_increasing_subsequences(arr))


if __name__ == "__main__":
    main()
