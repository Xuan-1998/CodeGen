def solution():
    t = int(input())
    memo = {}
    
    def helper(n):
        if (n,) in memo:
            return memo[(n,)]
        if n == 1:
            return 1
        
        val = int(str(n)[:-1] + str(int(str(n)[-1]) + 1))
        
        if len(str(val)) < len(str(n)):
            return 1 + helper(len(str(val)))
        elif len(str(val)) > len(str(n)):
            return helper(len(str(val)))
        else:
            return 2 + helper(len(str(val)))
    
    for _ in range(t):
        n, m = map(int, input().split())
        res = (helper(n) - 1) % (10**9 + 7)
        print(res)

if __name__ == "__main__":
    solution()
