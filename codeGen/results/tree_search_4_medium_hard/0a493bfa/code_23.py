def max_beauty(n, m, arr, bad_primes):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dp[i][i] = sum(arr[:i])
        
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length
            if bad_primes & (1 << (j - 1)):
                # Case 3: p is present in both halves
                left_max = dp[i][i]
                right_max = dp[j - 1][j - 1]
                
                # Find the maximum beauty by considering different cases
                max_beauty = max(left_max + i, right_max - (n - j), left_max + right_max)
            else:
                # Case 1: p is not present in the subarray
                left_max = dp[i][i]
                right_max = dp[j - 1][j - 1]
                
                # Find the maximum beauty by considering different cases
                max_beauty = max(left_max + right_max, i * (arr[i - 1] if i > 0 else 0))
            
            dp[i][j] = max_beauty
    
    return dp[1][n]

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = set(int(x) for x in input().split())

print(max_beauty(n, m, arr, bad_primes))
