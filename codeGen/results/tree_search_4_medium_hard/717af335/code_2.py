def find_min_xor(A, B):
    memo = {}
    
    def dfs(x):
        if x in memo:
            return memo[x]
        
        y = A - x
        if B == x ^ y:
            return x
        
        memo[x] = float('inf')
        for i in range(x + 1):
            res = dfs(i)
            if res != float('inf'):
                memo[x] = min(memo[x], res)
        
        return memo[x]
    
    min_xor = dfs(A)
    if min_xor == float('inf'):
        print(-1)
    else:
        for x in range(min_xor, A + 1):
            y = A - x
            if B == x ^ y:
                print(f"{x} {y}")
                break

A = int(input())
B = int(input())

find_min_xor(A, B)
