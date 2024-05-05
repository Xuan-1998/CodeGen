def max_beauty(n, m, a, b):
    # Initialize the maximum beauty to 0
    max_beauty = 0
    
    while True:
        # Loop through each element in the array
        for i in range(n):
            # Calculate the GCD of a[i] with the rest of the array
            gcd = a[i]
            for j in range(i):
                gcd = abs(gcd - a[j])
            for j in range(i+1, n):
                gcd = abs(gcd - a[j])
            
            # Apply the operation: replace a[i] with the calculated GCD
            a[i] = gcd
        
        # Update the maximum beauty by calling the function f(s) on the new array
        max_beauty = f(s)
        
        # Check if no further simplification is possible
        simplified = True
        for i in range(n):
            if a[i] != 1:
                simplified = False
                break
        
        if simplified:
            break
    
    return max_beauty

def f(s):
    # Define the function f(s) here...
    pass

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(max_beauty(n, m, a, b))
