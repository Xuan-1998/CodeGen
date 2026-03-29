# Read input
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    # Initialize result
    res = str(n)
    
    # Apply operations
    for i in range(m):
        temp = ''
        for d in str(res):
            if d != '9':
                temp += str(int(d) + 1)
            else:
                temp += '0'
        res = temp
    
    # Print answer
    print(len(str(res)) % (10**9 + 7))
