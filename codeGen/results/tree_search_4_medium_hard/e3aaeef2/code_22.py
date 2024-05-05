import heapq

def solve():
    t = int(input())
    memo = {}

    def helper(n, m):
        if (n, m) in memo:
            return memo[(n, m)]
        
        res = 0
        while n > 0:
            last_digit = n % 10
            n //= 10
            res += 1
            
            if last_digit == 9:
                break

        new_n = (10**(res-1)) + ((m+1) // res)
        
        for _ in range(m-res+1):
            new_n = int(str(new_n).zfill(res))
            
            for i in range(len(str(new_n))):
                last_digit = int(str(new_n)[i])
                new_n //= 10
                new_n += last_digit + 1
            
            new_n = int(str(new_n).lstrip('0') or '0')
        
        res2 = len(str(new_n))
        memo[(n, m)] = res2
        return res2

    for _ in range(t):
        n, m = map(int, input().split())
        print(helper(n, m) % (10**9 + 7))

if __name__ == "__main__":
    solve()
