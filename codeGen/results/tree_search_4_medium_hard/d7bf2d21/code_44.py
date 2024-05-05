import sys

def longest_increasing_subsequences(arr):
    dp = [1] * len(arr)
    max_length = 1
    
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        max_length = max(max_length, dp[i])
    
    return sum(1 for x in dp if x == max_length)

if __name__ == "__main__":
    input_array = list(map(int, input().split()))
    print(longest_increasing_subsequences(input_array))
