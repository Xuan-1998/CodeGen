def count_good_subsequences(a):
    MOD = 10**9 + 7
    n = len(a)
    
    def dfs(k, seen=None):
        if k > n:  # reached end of array
            return 0
        
        if k == n:  # last element
            if a[-1] % k != 0:
                return 0
            return 1
        
        res = 0
        if seen is None or a[k] % k != 0:  # current element not divisible by k
            res += dfs(k+1, set())  # no good subsequences ending with this element
        
        if seen is None:
            seen = set()
            res += dfs(k+1, seen | {a[k]})  # consider all subsequences ending with this element
        
        return res % MOD
    
    return dfs(1)
