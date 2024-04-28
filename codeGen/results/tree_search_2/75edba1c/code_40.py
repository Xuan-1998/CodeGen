from collections import defaultdict

def count_subarrays(N, K, Arr):
    max_val = 0
    res = 0
    
    for i in range(N):
        max_val = max(Arr[i], max_val)
        if max_val > K:
            res += N - i
            break
    
    return res
