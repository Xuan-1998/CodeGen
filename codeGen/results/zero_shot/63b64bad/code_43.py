def process_sequence():
    n = int(input())
    sequence = list(map(int, input().split()))
    
    results = []
    for a_x in sequence:
        x, y = 1, 0
        while x <= n and a_x > 0:
            x += a_x
            y += a_x
            a_x -= 1 if a_x == 1 else -a_x
            
            if x <= 0 or x > n:
                results.append(-1)
                break
        else:
            results.append(y)
            
    print(*results, sep='\n')

process_sequence()
