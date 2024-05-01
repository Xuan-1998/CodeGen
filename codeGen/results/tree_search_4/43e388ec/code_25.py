def solve():
    a, b = map(int, input().split())
    dp = [0] * (min(a.bit_length(), b.bit_length()) + 1)
    
    ah, bh = a, b
    
    for i in range(min(a.bit_length(), b.bit_length()) + 1):
        if (a >> i) & 1:
            ah ^= 1 << i
            dp[i] += ah % (10**9 + 7)
        else:
            bh >>= 1
            dp[i] += bh % (10**9 + 7)
    
    print(sum(dp) % (10**9 + 7))

if __name__ == "__main__":
    solve()
