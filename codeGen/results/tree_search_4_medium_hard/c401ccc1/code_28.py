from collections import deque

def infinite_zoo(q):
    dp = [[False] * (1 << 30) for _ in range(2**30)]
    
    for i in range(q):
        u, v = map(int, input().split())
        
        if dp[u][v]:
            print("YES")
        else:
            queue = deque([(u, 0)])
            while queue:
                curr_u, last_bit_set = queue.popleft()
                
                for next_u in range(2**30):
                    if not (curr_u & next_u) and (curr_u | next_u) == v:
                        dp[v][v] = True
                        print("YES")
                        return
                        
                for j in range(30, -1, -1):
                    if ((1 << j) & curr_u) and not ((1 << j) & v):
                        queue.append((next_u := (curr_u ^ (1 << j)), last_bit_set | 1 << j))
                        
            print("NO")
