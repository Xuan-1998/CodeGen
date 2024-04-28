def count_subarrays(N, K, Arr):
    max_val = 0
    count = 0
    for i in range(N):
        max_val = max(Arr[i], max_val)
        if max_val > K:
            count += N - i
            max_val = Arr[i]
    return count

N = int(input())
K = int(input())
Arr = list(map(int, input().split()))
print(count_subarrays(N, K, Arr))
