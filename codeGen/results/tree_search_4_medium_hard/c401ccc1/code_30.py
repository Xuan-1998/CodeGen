from sys import stdin

def solve():
    q = int(stdin.readline())
    dp = [False] * (1 << 30)
    
    for _ in range(q):
        u, v = map(int, stdin.readline().split())
        
        # Perform bitwise AND operation between u and all vertices
        for w in range(1 << 30):
            if (u & w) == w:
                dp[w] = True
        
        found_path = False
        for w in range(1 << 30):
            if (u & w) == w and dp[w]:
                found_path = True
                break
        
        print("YES" if found_path else "NO")

if __name__ == "__main__":
    solve()
