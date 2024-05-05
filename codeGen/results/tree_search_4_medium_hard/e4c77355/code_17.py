def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = {x: 1 for x in arr}  # Initialize the dictionary with values from array

    for i in range(n):
        for j in range(i):  # Iterate through all previous elements
            if arr[i] > arr[j]:  # If current element is greater than previous one
                dp[arr[i]] = max(dp.get(arr[i], 0), dp[arr[j]] + 1)  # Update the longest subsequence

    return max(dp.values())  # Return the maximum length of increasing subsequences


def main():
    arr = list(map(int, input().split()))
    print(longest_increasing_subsequence(arr))


if __name__ == "__main__":
    main()
