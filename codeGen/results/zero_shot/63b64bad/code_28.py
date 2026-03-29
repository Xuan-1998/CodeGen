code_block_start
n = int(input())
seq = list(map(int, input().split()))
final_y_values = []

for i in range(1, n):
    x = 1
    y = 0
    y_val = 0
    
    # Simulate the program until it terminates
    while True:
        if x > n or x <= 0:
            break
        a_x = seq[x-1]
        x += a_x
        y += a_x
        
        # Update y_val for this sequence run
        y_val = y
    
    final_y_values.append(y_val)
    
print("\n".join(map(str, final_y_values)))
code_block_end
