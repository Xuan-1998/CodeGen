import sys

def solve():
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        if a[i - 1] % i == 0:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 0
    
    total_good_subseqs = dp[-1]
    print(total_good_subseqs % (10**9 + 7))

if __name__ == "__main__":
    solve()
