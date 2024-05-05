===BEGIN CODE===
from heapq import heappush, heappop

def solve():
    n = int(input())
    seq = list(map(int, input().split()))
    
    memo = {}  # Memoization dictionary
    
    def process_state(x, y):
        if (x, y) in memo:
            return memo[(x, y)]
        
        result = -1
        while x > 0 and x <= n:
            a_x = seq[x-1]
            x += a_x
            y += a_x
            x -= a_x
            
            # Check if the program terminates (i.e., x becomes negative or exceeds n)
            if x < 0 or x > n:
                result = -1
                break
            
        memo[(x, y)] = result
        return result
    
    for i in range(1, n):
        heappush(heap, (process_state(i, 0), i))
    
    while heap:
        val, _ = heappop(heap)
        if val != -1:
            print(val)
            break
    else:
        print(-1)
    
    ===END CODE===
