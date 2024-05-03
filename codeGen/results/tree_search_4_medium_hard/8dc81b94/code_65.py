import sys

def solve():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    
    dp = [False] * (n + 1)
    target = sum(arr)
    
    for i in range(n - 1, -1, -1):
        if target <= 0:
            dp[i] = True
            break
        elif not dp[i]:
            dp[i] = (target >= arr[i]) and dp[i + 1]
        
    print("YES" if dp[0] else "NO")

if __name__ == "__main__":
    solve()
