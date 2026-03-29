import sys

def read_array():
    array = []
    while True:
        line = input().strip()
        if line == "":
            break
        array.append(int(line))
    return array

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], 1 + dp[j])

    return max(dp)

if __name__ == "__main__":
    array = read_array()
    print(longest_increasing_subsequence(array))
