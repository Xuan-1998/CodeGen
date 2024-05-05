from collections import defaultdict

def simulate_program(n, sequence):
    dp = {(x, y): -1 for x in range(1, n+2) for y in range(n+1)}
    
    def get_final_y(x, y):
        if (x, y) not in dp:
            new_x = x + sequence[x-1]
            new_y = y + sequence[x-1]
            if (new_x, new_y) not in dp and 0 <= new_x <= n:
                dp[(new_x, new_y)] = -1
                return get_final_y(new_x, new_y)
            elif (new_x, new_y) not in dp:
                return y
            else:
                return -1
        
        if dp[(x, y)] == -1:
            return -1
        else:
            return dp[(x, y)]
    
    for x in range(1, n+1):
        final_y = get_final_y(x, 0)
        print(final_y)

n = int(input())
sequence = list(map(int, input().split()))
simulate_program(n, sequence)
