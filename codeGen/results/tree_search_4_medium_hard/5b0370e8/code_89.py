import sys

def solve():
    n, k = map(int, input().split())
    dp = [[0] * (1 << k) for _ in range(k + 1)]
    
    # Initialize base case: there is only one way to make bitwise AND 0 and bitwise XOR i, which is the array [i]
    for i in range(1 << k):
        dp[0][i] = 1
    
    for i in range(1, n + 1):
        for j in range(k, -1, -1):
            if (i >> j) & 1:
                # If the ith number has the jth bit set, then we can make bitwise AND j and bitwise XOR (j ^ i)
                dp[j][dp[j-1][i^1] + (i>>j)] += 2**(k-j-1)
            else:
                # If the ith number does not have the jth bit set, then we can make bitwise AND j and bitwise XOR j
                dp[j][dp[j][j]] += 2**(k-j-1)
    
    count = 0
    for i in range(1 << k):
        if all((a & b) >= a for a in range(n)) and all(a ^ b <= max(range(n)) for a, b in zip(range(i), reversed(list(bin(i)[2:].zfill(k))))):
            count += dp[k][i]
    
    print(count % (10**9 + 7))

if __name__ == "__main__":
    solve()
