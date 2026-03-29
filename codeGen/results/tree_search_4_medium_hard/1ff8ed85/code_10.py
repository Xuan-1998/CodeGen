def can_obtain_sequence():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        memo = {}
        
        def dfs(n, val):
            if (n, val) in memo: 
                return memo[(n, val)]
            
            if n == 0:
                return True
            
            for i in range(1, val+1):
                if i != b[-n] and dfs(n-1, i): 
                    memo[(n, val)] = True
                    return True
            
            memo[(n, val)] = False
            return False
        
        if dfs(n, 0): 
            print("YES")
        else:
            print("NO")

can_obtain_sequence()
