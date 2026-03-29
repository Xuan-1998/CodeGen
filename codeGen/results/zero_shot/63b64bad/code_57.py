def calculate_y(n):
    sequence = list(map(int, input().split()))
    y_values = []
    
    for a_x in sequence:
        x = 1
        y = 0
        
        while x > 0 and x <= n:
            x += a_x
            y += a_x
            if x > 0:
                x -= a_x
                y += a_x
        
        if x <= 0 or x > n:
            y_values.append(-1)
        else:
            y_values.append(y)
    
    print('\n'.join(map(str, y_values)))

if __name__ == "__main__":
    n = int(input())
    calculate_y(n)
