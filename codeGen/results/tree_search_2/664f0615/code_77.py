import sys

def solve():
    initialSpeed, finalSpeed, time, maxAllowedChange = [int(x) for x in input().split()]
    
    dp = [[0] * (finalSpeed + 1) for _ in range(initialSpeed + 1)]
    
    for i in range(1, initialSpeed + 1):
        for j in range(i, finalSpeed + 1):
            for k in range(min(i, j), maxAllowedChange + 1):
                seg = [0]
                for l in range(k + 1):
                    if l > 0:
                        seg.append(seg[l - 1] + min((j - i) // (l + 1), k))
                dp[i][j] = max(dp[i][j], seg[-1] + 1)
    
    print(dp[initialSpeed][finalSpeed])

if __name__ == "__main__":
    solve()
