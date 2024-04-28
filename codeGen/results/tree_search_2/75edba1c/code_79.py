from itertools import combinations

def count_subarrays(Arr, K):
    n = len(Arr)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        max_val = max(Arr[i-1])
        if max_val > K:
            dp[i] = dp[i-1]
        else:
            for j in range(i):
                max_subarray = max(Arr[j:i+1])
                if max_subarray > K:
                    dp[i] += dp[j-1]

    return sum(dp)

if __name__ == "__main__":
    n, K = map(int, input().split())
    Arr = list(map(int, input().split()))
    print(count_subarrays(Arr, K))
