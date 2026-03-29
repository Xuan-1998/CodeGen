from collections import defaultdict

def solve():
    n = int(input())
    seq = list(map(int, input().split()))
    
    memo = defaultdict(lambda: (-1, 0))
    
    for i in range(2, n+1):
        x, y = memo[i-1]
        a_i = seq[i-1]
        
        while x <= 0 or x > n:
            break
        
        x += a_i
        y += a_i
        x -= a_i
        
        if (x, y) in memo:
            return y
        
        memo[x] = (x, y)
    
    print(-1)

if __name__ == "__main__":
    solve()
