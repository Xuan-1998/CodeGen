def min_function_value():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        
        result = 0
        for i in range(1, n-1):
            if a[i] <= s:
                x = 0
                y = s - (s - a[i])
            else:
                x = s
                y = 0
            
            result += x * a[i+1] + y * a[i+2]
        
        print(result)
