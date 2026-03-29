def solve():
    q = int(input())
    for _ in range(q):
        u, v = map(int, input().split())
        
        # check if there is a path from u to v
        if is_path(u, v):
            print("YES")
        else:
            print("NO")

def is_path(u, v):
    if u & v == 0: 
        return False
    
    while u != v:
        if (u & v) == 0:
            return False
        
        u &= v
    
    return True

if __name__ == "__main__":
    solve()
