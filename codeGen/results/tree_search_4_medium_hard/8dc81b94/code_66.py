import sys

def solve():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        if dp[i - 1]:
            if all(x == arr[i - 1] for x in arr[:i]):
                dp[i] = True
            else:
                dp[i] = False
        else:
            dp[i] = False
    
    print("YES" if dp[-1] else "NO")

if __name__ == "__main__":
    solve()
