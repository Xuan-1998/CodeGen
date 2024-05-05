import sys

def read_input():
    return [int(x) for x in input().split()]

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [[0] * (max(arr) + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        last_index = -1
        for x in arr[:i]:
            if binary_search(dp[i-1], x, last_index):
                dp[i][x] = i
                last_index = dp[i-1].index(x)
        
    return max(max(row) for row in dp)

def binary_search(arr, target, last_index):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target and mid > last_index:
            low = mid + 1
        elif arr[mid] >= target:
            high = mid - 1
        else:
            return True
    return False

if __name__ == "__main__":
    input_arr = read_input()
    print(longest_increasing_subsequence(input_arr))
