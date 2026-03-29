def length_after_operations():
    dp = {}
    
    def process(n, m):
        if (n, m) in dp:
            return dp[(n, m)]
        
        if n == 0 and m > 0:
            return process(1, m-1)
        
        if m == 0:
            return len(str(n))
        
        result = 0
        while n > 0:
            d = n % 10
            n //= 10
            d += 1
            result += (d != 0)  # count the digits
        return result
        
    t = int(input())
    
    for _ in range(t):
        n, m = map(int, input().split())
        print(process(n, m) % (10**9 + 7))
