import sys
from collections import defaultdict

def main():
    read = lambda: [int(x) for x in input().split()]
    write = lambda *a: print(*a)

    n, q = read()
    sign_values = read()[0:n]
    dp = [[float('inf')] * (n+1) for _ in range(n+1)]
    
    # Initialize base cases
    for i in range(n+1):
        dp[i][0] = 0
    for j in range(n+1):
        dp[0][j] = 0

    prefix_sum = defaultdict(int)
    sign_sum = sum(sign_values)

    write(sign_sum)

    for _ in range(q):
        l, r = read()
        write(min(dp[l-1][r] - (sign_sum - 2*sum(sign_values[i] for i in range(l-1))), 
                   dp[0][r-l+1]))

if __name__ == "__main__":
    main()
