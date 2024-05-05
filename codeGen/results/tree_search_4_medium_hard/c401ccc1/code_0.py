import sys
input = sys.stdin.readline

def main():
    q = int(input())
    dp = [False] * (2**30)
    dp[0] = True
    
    for _ in range(q):
        u, v = map(int, input().split())
        
        while v > 0:
            if not dp[v]:
                break
            v &= u
            
        print("YES" if dp[v] else "NO")

if __name__ == "__main__":
    main()
