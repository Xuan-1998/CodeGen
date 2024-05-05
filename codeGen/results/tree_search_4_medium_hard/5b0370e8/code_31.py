import sys

def solve():
    t = int(input())
    MOD = 10**9 + 7
    memo = {}
    
    for _ in range(t):
        n, k = map(int, input().split())
        ans = [0] * (k + 1)
        
        for i in range(n + 1):
            for j in range(k, -1, -1):
                if i == 0:
                    ans[j] += 1
                    continue
                
                if j == 0:
                    ans[j] += memo.get((i - 1, k), 0)
                    continue
                
                last_bit = (k - 1) & (~j)
                ans[j] += memo.get((i - 1, last_bit), 0)
        
        print(sum(ans) % MOD)

if __name__ == "__main__":
    solve()
