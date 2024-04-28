import sys

def count_subarrays(arr, K):
    N = len(arr)
    dp = [[0] * (N+1) for _ in range(N+1)]

    for i in range(1, N+1):
        max_val = max(arr[i-1])
        for j in range(i, N+1):
            if arr[j-1] > K:
                max_val = max(max_val, arr[j-1])
            dp[i][j] = dp[i-1][j-1] + (max_val > K)

    return sum(dp[N][i] for i in range(N))

def main():
    N, K = map(int, input().split())
    Arr = list(map(int, input().split()))
    print(count_subarrays(Arr, K))

if __name__ == "__main__":
    main()
