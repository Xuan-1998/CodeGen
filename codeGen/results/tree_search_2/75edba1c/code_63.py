from typing import List

def count_subarrays(arr: List[int], K: int) -> int:
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        max_element = max(arr[:i])
        if max_element > K:
            dp[i] = dp[i - 1]
            for j in range(i):
                if arr[j:i+1].count(max(arr[j:i+1])) == 1 and max(arr[j:i+1]) > K:
                    dp[i] += 1
    return sum(dp)

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(count_subarrays(arr, k))
