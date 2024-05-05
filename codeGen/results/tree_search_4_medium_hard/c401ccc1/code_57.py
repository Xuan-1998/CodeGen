import sys

def solve():
    q = int(input())
    dp = [[False] * (2**30) for _ in range(2**30)]
    
    for _ in range(q):
        u, v = map(int, input().split())
        
        # Start from vertex v and try to reach vertex u
        stack = [v]
        visited = {v}
        while stack:
            cur = stack.pop()
            if cur == u:
                print("YES")
                return
            
            for neighbor in range(2**30):
                if (cur & neighbor) != 0:  # If there's an outgoing edge
                    if not dp[v][neighbor]:
                        stack.append(neighbor)
                        visited.add(neighbor)
                        dp[neighbor][cur] = True
        
        print("NO")

solve()
