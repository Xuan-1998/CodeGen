def count_subarrays(N, K, Arr):
    dp = {}
    ans = 0

    for i in range(N):
        max_val = 0
        for j in range(i, N):
            max_val = max(max_val, Arr[j])
            if max_val > K:
                ans += 1
                break
        dp[(i, max_val)] = ans

    return sum(dp.values())

N, K = map(int, input().split())
Arr = list(map(int, input().split()))
print(count_subarrays(N, K, Arr))
