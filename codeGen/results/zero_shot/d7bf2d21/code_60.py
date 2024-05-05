import sys

def find_LIS_length(arr):
    n = len(arr)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    
    print(find_LIS_length(arr))

if __name__ == "__main__":
    main()
