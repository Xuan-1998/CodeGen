=~=CODE START~~~~

def beauty_contest(t, l, r):
    MOD = 10**9 + 7
    
    memo = {1: 0}
    
    for n in range(2, r+1):
        memo[n] = float('inf')
        
        for k in range(l, n//2+1):
            if k not in memo:
                memo[k] = beauty_contest(k)
            
            memo[n] = min(memo[n], memo[k] + 1)
    
    return sum(t * (memo[n] - l) for n in range(l, r+1)) % MOD

t, l, r = map(int, input().split())
print(beauty_contest(t, l, r))
