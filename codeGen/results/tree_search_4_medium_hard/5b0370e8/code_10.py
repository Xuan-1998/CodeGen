MOD = 10**9 + 7

def solve(n, k):
    memo = {}
    
    def dfs(i, and_result):
        if (i, and_result) in memo:
            return memo[(i, and_result)]
        
        result = 0
        
        for j in range(2**k):
            xor_result = 0
            and_mask = and_result
            
            for bit in range(k-1, -1, -1):
                if (j >> bit) & 1:
                    xor_result ^= (1 << bit)
                    and_mask &= ~(1 << bit)
                
                if and_mask == 0 or (and_mask & (1 << (k-1))): break
                result = (result + dfs(i+1, and_mask)) % MOD
            
            memo[(i, and_result)] = result
        return result
    
    return dfs(0, (1 << k) - 1)

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))
