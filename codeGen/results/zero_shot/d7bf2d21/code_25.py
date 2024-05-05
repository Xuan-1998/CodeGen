import sys

def read_input():
    return list(map(int, input().split()))

def lis_length(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

def main():
    arr = read_input()
    max_length = lis_length(arr)
    count = sum(1 for x in arr if len(lis_length([x] + arr)) == max_length)
    print(count)

if __name__ == "__main__":
    main()
