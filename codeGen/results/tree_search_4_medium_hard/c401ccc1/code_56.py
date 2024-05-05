def dfs(v, visited, memo):
    if v in visited:
        return False
    visited.add(v)
    
    if v & (v) == 0:  # no outgoing edge from v
        return True
    
    if v in memo:
        return memo[v]
    
    result = False
    for w in range(2**30):
        if w & v:  # there's an edge from v to w
            result |= dfs(w, visited, memo)
    
    memo[v] = result
    return result

def solve():
    q = int(input())
    memo = {}
    for _ in range(q):
        u, v = map(int, input().split())
        visited = set()
        print("YES" if dfs(v, visited, memo) else "NO")

if __name__ == "__main__":
    solve()
