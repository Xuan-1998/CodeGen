def count_blocks():
    # Initialize the result with 1
    res = 1
    
    for mi in m:
        # Calculate the length of the current block
        len_block = min(n, mi)
        
        # Calculate how many numbers are greater than or equal to mi
        num_greater = len_block - (mi - 1) if mi > 1 else 0
        
        # Update the result using the formula: res *= (n-mi+num_greater+1)
        res = (res * ((n-mi)+num_greater+1)) % (10**9 + 7)
    
    return int(res)

print(count_blocks())
