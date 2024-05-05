import sys

def find_lis_count(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], 1 + dp[j])

    max_length = max(dp)
    return sum(1 for x in dp if x == max_length)

if __name__ == "__main__":
    input_arr = list(map(int, input().split()))
    print(find_lis_count(input_arr))
