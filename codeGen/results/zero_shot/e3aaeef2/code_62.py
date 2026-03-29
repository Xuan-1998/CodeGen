# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read n and m
    n, m = map(int, input().split())
    
    # Initialize a variable to store the length of the resulting number
    result_len = 0
    
    for i in range(m):
        # Convert n to a string to easily get each digit
        str_n = str(n)
        
        # Replace each digit with its successor (d + 1) and convert back to integer
        n = int(''.join(str(int(d) + 1) if d != '9' else '0' for d in str_n))
        
        # Increment result_len by the number of digits added/deleted in this operation
        result_len += (str(n).count('0') - str_n.count('0'))
    
    # Print the length of the resulting number modulo 10^9+7
    print(result_len % (10**9 + 7))
