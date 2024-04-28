import sys

def solve(N, K, arr):
    dp = [[False]*N for _ in range(N)]
    res = 0
    for i in range(N-1, -1, -1):
        max_val = 0
        for j in range(i, N):
            if arr[j] > K:
                max_val = arr[j]
                break
            elif arr[j] > max_val:
                max_val = arr[j]
        for k in range(i-1, -1, -1):
            if dp[k+1][j]:
                dp[i][k] = True
                res += 1
    return res

if __name__ == "__main__":
    N = int(input())
    K = int(input())
    arr = list(map(int, input().split()))
    print(solve(N, K, arr))
