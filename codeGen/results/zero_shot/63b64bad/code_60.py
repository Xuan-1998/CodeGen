import sys

n = int(input())
sequence = list(map(int, input().split()))

for i in range(2, n+1):
    x = 1
    y = 0
    
    while True:
        if x <= 0 or x > i:
            print(-1)
            break
        x += sequence[x]
        y += sequence[x]
        x -= sequence[x]
    
    print(y)
