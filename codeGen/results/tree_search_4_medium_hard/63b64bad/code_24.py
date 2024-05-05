from collections import defaultdict

def calculate_y(n, sequence):
    memo = defaultdict(int)
    def dfs(x, y, terminated):
        if terminated:
            return y
        if (x, y, terminated) in memo:
            return memo[(x, y, terminated)]
        
        if x <= 0 or x > n:
            return -1
        
        new_x = x + sequence[x]
        new_y = y + sequence[x]
        new_terminated = False
        
        for _ in range(sequence[x]):
            x -= sequence[x]
            y += sequence[x]
        
        result = dfs(new_x, new_y, new_terminated)
        if result == -1:
            return -1
        else:
            memo[(x, y, terminated)] = result
            return result
    
    for i in range(2, n+1):
        sequence[i-1] += 1
    return dfs(1, 0, False)

n = int(input())
sequence = list(map(int, input().split()))
for i in range(n-1):
    print(calculate_y(n, [x//a for a in sequence]))
