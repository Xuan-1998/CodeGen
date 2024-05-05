import sys

def solve():
    n = int(sys.stdin.readline())
    sequence = list(map(int, sys.stdin.readline().split()))
    
    for i in range(1, n):
        x = 1
        y = 0
        while True:
            if x <= 0 or x > n:
                break
            y += sequence[x]
            x += sequence[x]
            x -= sequence[x]
        
        print(y)
