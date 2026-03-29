import sys

def find_lis_count(arr):
    n = len(arr)
    dp = [1] * n  # dynamic programming table
    max_length = 1  # maximum length found so far
    count = 0  # count of longest increasing subsequences

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        if dp[i] > max_length:
            max_length = dp[i]
        if dp[i] == max_length:
            count += 1

    return count

def main():
    n = int(input())  # read the input array size
    arr = list(map(int, input().split()))  # read the unsorted array

    print(find_lis_count(arr))  # find and print the number of longest increasing subsequences

if __name__ == "__main__":
    main()
