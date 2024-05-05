def max_beauty(arr, bad_primes):
    memo = {}

    def dp(k, v):
        if (k, v) in memo:
            return memo[(k, v)]
        
        if k == len(arr) - 1:
            return v
        
        best = 0
        for i in range(len(bad_primes)):
            if arr[k] in bad_primes[i]:
                best = max(best, dp(k + 1, v - 1))
                break
        else:
            for good_prime in [2]:  # You can add more good prime numbers here
                if arr[k] % good_prime == 0:
                    best = max(best, dp(k + 1, v + 1))
        
        memo[(k, v)] = best
        return best
    
    return dp(0, 0)
