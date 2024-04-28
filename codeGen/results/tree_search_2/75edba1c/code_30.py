from collections import defaultdict

def count_subarrays(N, K, Arr):
    dp = defaultdict(int)
    
    for i in range(len(Arr)):
        for k in range(i + 1):
            if not (i, k) in dp:
                max_val = max(Arr[k:i+k+1])
                dp[(i, k)] = 1 if max_val > K else 0
    
    return sum(dp.values())

# Input
N = int(input())
K = int(input())
Arr = list(map(int, input().split()))

# Output
print(count_subarrays(N, K, Arr))
