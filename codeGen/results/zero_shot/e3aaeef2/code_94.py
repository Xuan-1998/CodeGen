import sys

def solve(n, m):
    # Initialize the result with the initial value of n
    res = str(n)
    
    # Apply the operations for m times
    for _ in range(m):
        new_res = ''
        carry = 0
        for d in res:
            # Replace each digit with its incremented value (d + 1)
            new_d = int(d) + 1
            # Convert the new digit to a string and add it to the result
            new_res += str(new_d)
            # Update the carry if necessary
            if new_d >= 10:
                carry = 1
        # If there's a carry, prepend it to the result
        if carry:
            new_res = '1' + new_res
        res = new_res
    
    # Return the length of the resulting number modulo 10^9+7
    return len(res) % (10**9 + 7)

# Read input from stdin
t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(solve(n, m))
