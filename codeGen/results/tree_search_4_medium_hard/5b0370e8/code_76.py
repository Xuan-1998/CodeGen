import sys

def solve():
    t = int(input())
    
    for _ in range(t):
        n, k = map(int, input().split())
        
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(k + 1):
                if bin(i).count('1') == k:
                    and_count = 2**k - 1
                else:
                    and_count = 0
                
                xor_count = sum((a >> b) & 1 for a in range(i)) % 2
                
                dp[i][j] = (and_count >= xor_count)
                
        total = sum(1 if dp[n][i] else 0 for i in range(k + 1))
        
        print(total % (10**9 + 7))

if __name__ == "__main__":
    solve()
