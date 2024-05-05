import sys

def solve():
    q = int(input())
    dp = [[False] * (2**20) for _ in range(2**20)]
    
    for _ in range(q):
        u, v = map(int, input().split())
        
        if not any((u & w) == w and not dp[w][v] for w in range(u)):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()
