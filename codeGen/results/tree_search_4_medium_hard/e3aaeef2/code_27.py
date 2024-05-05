def solve():
    t = int(input())
    memo = {}
    
    def update_state(state):
        n, k = state
        if (n, k) in memo:
            return memo[(n, k)]
        
        next_n = 0
        for i in range(n):
            d = (k % 10)
            next_d = (d + 1) % 10
            next_n = next_n * 10 + next_d
            
            if i < n - 1:
                k //= 10
        
        memo[(n, k)] = update_state((next_n.bit_length(), (k + 1) % 1000000007))
        
        return memo[(n, k)]
    
    for _ in range(t):
        n, m = map(int, input().split())
        print(update_state((n.bit_length(), m)) % 1000000007)

solve()
