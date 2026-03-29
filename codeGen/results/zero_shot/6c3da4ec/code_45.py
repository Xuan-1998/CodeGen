def max_bit_or():
    n = int(input())
    s = input()
    
    # Initialize maximum possible value
    max_val = 0
    
    for i in range(n):
        for j in range(i+1, n):
            # Calculate bitwise OR of substrings
            val = int(s[i:j+1], 2)
            
            # Update maximum possible value
            if val > max_val:
                max_val = val
                
    print(bin(max_val)[2:])
