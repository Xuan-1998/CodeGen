def count_subarrays(N, K, Arr):
    memo = {}
    count = 0
    for i in range(N):
        if Arr[i] > K:
            max_val = Arr[i]
            count += 1
        else:
            max_val = 0
            count = 0
        memo[(i, max_val)] = count
    return sum(memo.values())

# Read input from stdin
N, K = map(int, input().split())
Arr = list(map(int, input().split()))

print(count_subarrays(N, K, Arr))
