import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))

for i in range(2, n+1):
    x = 1
    y = 0
    
    while True:
        x += sequence[i-1]
        y += sequence[i-1]
        
        if x <= 0 or x > n:
            break
        
        x -= sequence[i-1]
        y += sequence[i-1]
    
    print(y)
