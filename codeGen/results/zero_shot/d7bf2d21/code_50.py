import sys

def find_lis(arr):
    n = len(arr)
    dp = [[1] * n for _ in range(n)]
    
    max_length = [0] * (n + 1)

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i][j] = dp[j][i - 1] + 1
                max_length[i] = max(max_length[i], dp[i][j])
    
    return len(set(max_length))

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(find_lis(arr))
