import math

def main():
    n = int(input())
    
    # Calculate the total number of ways to build towers
    total_ways = 2**n
    
    # Initialize the result variable
    result = 1
    
    # Check if there are enough towns for building towers
    if n < 3:
        print(result)
        return
    
    # Check if there are enough signal powers for each tower
    if n > 1:
        total_ways *= math.factorial(n) // (math.factorial(n-2) * 2)
    
    # Calculate the final result
    result = total_ways % (998244353)
    
    print(result)

if __name__ == "__main__":
    main()
