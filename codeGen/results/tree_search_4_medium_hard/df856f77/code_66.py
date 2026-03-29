import sys

def min_operations(arr):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n):
        if arr[i-1] > arr[i]:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1]

    return dp[-1]

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(min_operations(arr))

if __name__ == "__main__":
    main()
