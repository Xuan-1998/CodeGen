import sys

def bfs(u, v):
    visited = set()
    queue = [(u, '')]
    
    while queue:
        node, path = queue.pop(0)
        
        if node == v:
            return "YES"
        
        for i in range(len(bin(node)[2:])):
            new_node = int('1' + bin(node)[2:] + '0'[i+1:], 2)
            
            if str(new_node) != str(node):
                if new_node not in visited:
                    visited.add(new_node)
                    queue.append((new_node, path + '1' + '0'[i+1:]))
    
    return "NO"

q = int(sys.stdin.readline())
for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    print("YES" if bfs(u, v) else "NO")
