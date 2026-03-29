def count_and_xor(n, k):
    MOD = 10**9 + 7
    dp = {i: [0] * (k + 1) for i in range(k + 1)}
    
    def and_or_xor(i, k):
        if i < 0:
            return 1
        if (i, k) in dp:
            return dp[(i, k)]
        
        count = 0
        for j in range(2**k - 1):
            if ((j >> i) & 1) == (((~j) >> i) & 1):
                count += and_or_xor(i-1, k-1)
        return (count + MOD) % MOD
    
    result = 0
    for _ in range(n):
        x = int(input())
        if x < 2**k:
            result = (result + and_or_xor(k-1, k)) % MOD
        else:
            break
    
    print(result)
