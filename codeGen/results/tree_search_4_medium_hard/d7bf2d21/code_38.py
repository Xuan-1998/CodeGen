from collections import defaultdict

def find_longest_increasing_subsequences(input_array):
    n = len(input_array)
    dp = [1] * n
    max_length = 0
    for i in range(1, n):
        for j in range(i):
            if input_array[i] > input_array[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        max_length = max(max_length, dp[i])
    
    return max_length

if __name__ == "__main__":
    array_size = int(input())
    arr = list(map(int, input().split()))
    print(find_longest_increasing_subsequences(arr))
