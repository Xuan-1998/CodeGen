def solve():
    n = int(input())
    sequence = list(map(int, input().split()))
    
    for i in range(1, n):
        x, y = 1, 0
        while True:
            # Perform step 2: increase both x and y by a_{x}
            x += sequence[x]
            y += sequence[x]
            
            # Perform step 3: increase y by a_{x} while decreasing x by a_{x}
            y += sequence[x]
            x -= sequence[x]
            
            if x <= 0 or x > n:
                break
        
        print(y)
