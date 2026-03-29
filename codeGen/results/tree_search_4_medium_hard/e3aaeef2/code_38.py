def solve():
    t = int(input())
    MOD = 10**9 + 7
    dp = {(1, 0): 1}
    
    for _ in range(t):
        n, m = map(int, input().split())
        
        if (n % 10 == 0 and m > 0) or (n < 10 and m > 0):
            ans = 1
        else:
            i = len(str(n))
            j = min(i - 1, m)
            
            while j >= 0:
                for k in range(10):
                    if (k == 9 and j == 0) or (dp.get((i, j), None) is not None):
                        break
                    new_i = i - (n // 10**i).count(k) + (n // 10**(i-1)).count(k)
                    dp[(new_i, j-1)] = min(dp.get((new_i, j-1)), dp.get((i, j), float('inf')))
                i -= 1
                j -= 1
            
            ans = i
        
        print(ans % MOD)

if __name__ == "__main__":
    solve()
