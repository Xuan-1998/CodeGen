from functools import lru_cache

def count_paths(arr, K):
    N = len(arr)
    dp_table = {}

    @lru_cache(maxsize=None)
    def get_dp(i, j, k):
        if (i, j, k) in dp_table:
            return dp_table[(i, j, k)]
        
        result = 0
        if i < N-1 and j < N-1:
            if k > 0:
                result = get_dp(i+1, j, k-arr[i][j]) + get_dp(i, j+1, k-arr[i][j])
            else: 
                result = 1
        dp_table[(i, j, k)] = result
        return result

    def solve():
        if K == 0:
            return 1
        elif (K > arr[0][0] and N > 1) or (K > arr[0][1] and N > 1):
            return 0
        else:
            return get_dp(0, 0, K)

    return solve()
